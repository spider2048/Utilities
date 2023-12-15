import os
import pefile
import requests
import struct
import argparse
import binascii
import logging
from tqdm import tqdm

logging.basicConfig(level=logging.INFO)
SYMBOL_SERVER = (
    "http://msdl.microsoft.com/download/symbols/{pdb_filename}/{guid}/{pdb_filename}"
)


def get_guid(src):
    pe = pefile.PE(src)
    i = pe.DIRECTORY_ENTRY_DEBUG[0]  # type: ignore
    H = lambda *x: binascii.hexlify(struct.pack(*x))

    return (
        b"".join(
            [
                H(">I", i.entry.Signature_Data1),
                b"-",
                H(">H", i.entry.Signature_Data2),
                b"-",
                H(">H", i.entry.Signature_Data3),
                b"-",
                H(">B", i.entry.Signature_Data4),
                H(">B", i.entry.Signature_Data5),
                b"-",
                binascii.b2a_hex(i.entry.Signature_Data6),
                b"-",
                H(">I", i.entry.Age).lstrip(b"0"),
            ]
        )
        .decode()
        .upper(),
        i.entry.PdbFileName.strip(b"\x00").decode(),
    )


def download_pdb(guid, pdb_filename, dst):
    guid = guid.replace("-", "")
    logging.debug("GUID: %s PDBFilename: %s", guid, pdb_filename)

    if os.path.isdir(dst):
        dst = os.path.join(dst, pdb_filename)

    download_link = SYMBOL_SERVER.format(pdb_filename=pdb_filename, guid=guid)
    logging.debug(download_link)

    r = requests.get(download_link, stream=True)
    assert r.status_code != 404, f"unable to download PDB from {download_link}"
    size = int(r.headers["Content-Length"])

    logging.info(
        "Downloading %s => %s (%.2f MB) ...", pdb_filename, dst, size / 1024**2
    )

    with open(dst, "wb+") as fd:
        with tqdm(total=size, unit_scale=1 / 1024, unit="KB") as pbar:
            for chunk in r.iter_content(chunk_size=8192):
                fd.write(chunk)
                pbar.update(8192)

            logging.info(
                "Finished downloading %s => %s (%d MB)",
                pdb_filename,
                dst,
                fd.tell() / 1024**2,
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-pe", required=True, help='path to exe/dll')
    parser.add_argument("-dst", required=False, help='path to destination PDB file')

    args = parser.parse_args()
    if not args.dst:
        args.dst = "."

    download_pdb(*get_guid(args.pe), args.dst)
