import argparse
import time
import os
import sys
import subprocess
import logging
import shlex
from typing import List, Dict

file_map :Dict[str, float] = {}
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("entr")

CLEAR = 'cls' if os.name == 'nt' else 'clear'

def run(cmd :List[str], wd :str):
    # Split if command is a single string
    if len(cmd) == 1: cmd = shlex.split(cmd[0])
    return subprocess.Popen(cmd, cwd=wd)

def verify(file_path: str):
    if os.path.exists(file_path):
        file_path = os.path.abspath(file_path)
        if os.path.isfile(file_path):
            file_map[file_path] = 0
        else:
            logger.error("%s is not a valid file", file_path)
    else:
        logger.error("%s doesn't exist", file_path)

def clear_screen():
    os.system(CLEAR)

def monitor(cmd: List[str], delay :float =1.0, timeout=-1, wd='.', clear=False):
    if timeout == -1:
        timeout = None

    def _check_files():
        for file, mtime in file_map.items():
            if not os.path.exists(file) or os.stat(file).st_mtime > mtime:
                logger.debug("Detected changes in %s", file)
                return True
        return False

    # Update all file(s)
    def update_files():
        keys = tuple(file_map.keys())
        for file_path in keys:
            try:
                stat = os.stat(file_path)
                file_map[file_path] = stat.st_mtime
            except FileNotFoundError:
                logger.info("couldn't stat %s, assuming deleted", file_path)
                del file_map[file_path]

    # Run the command
    def _process_changes(cmd: List[str], timeout: float|None):
        logger.info("running cmd on %s ...", time.asctime())
        t_start = time.time()
        proc = run(cmd, wd)
        exit_code = proc.wait(timeout)
        logger.info("command took %.2fs with exit code: %d", time.time() - t_start, exit_code)

    logger.info("Monitoring for changes [%d files]", len(file_map))
    while True:
        if _check_files():
            if clear: clear_screen()
            _process_changes(cmd, timeout)
            update_files()
        time.sleep(delay)

def main():
    parser = argparse.ArgumentParser(description='a cross-platform replacement for `entr`')
    parser.add_argument('-delay', default=1.0, type=float, help='delay to wait before polling')
    parser.add_argument('-timeout', default=-1, type=float, help='timeout for the command')
    parser.add_argument('-wd', default='.', type=str, help='working directory for the command')
    parser.add_argument('-clear', action='store_true', help='clear the screen on change')
    parser.add_argument('command', nargs='+', help='command to run')

    args = parser.parse_args()

    for file_path in sys.stdin.readlines():
        if file_path:
            verify(file_path.strip())

    monitor(args.command, delay=args.delay, timeout=args.timeout, wd=args.wd, clear=args.clear)

main()
