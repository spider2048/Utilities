# PDB Downloader

A utility to download PDBs from Microsoft Symbol Servers using the GUID

## Usage

First, install the dependencies:

```bash
pip install -r requirements.txt
```

Download a PDB by:

```bash
python pdb_download.py -pe "path/to/pe" -dst "path/to/pdb"
```

Example usage:

```bash
% python .\pdb_download.py -pe C:\Windows\explorer.exe
INFO:root:Downloading explorer.pdb => .\explorer.pdb (5.44 MB) ...
<progress bar>
```

Help:

```bash
% python pdb_download.py -h
usage: pdb_download.py [-h] -pe PE [-dst DST]

options:
  -h, --help  show this help message and exit
  -pe PE      path to exe/dll
  -dst DST    path to destination PDB file
```
