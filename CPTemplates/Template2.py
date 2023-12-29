import os
import sys
import time
import heapq
import itertools
import functools

MULTIPLE_TESTS = False


def inp():
    return list(map(int, input().split(" ")))


def solve():
    print("2 + 2 = 4")


def main():
    if MULTIPLE_TESTS:
        for _ in range(int(input())):
            solve()
    else:
        solve()


def local_main():
    sys.stdin = open("input.txt")
    main()


def local__entry():
    import logging
    import multiprocessing
    import pyperclip
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logger = logging.getLogger("AutoReload")
    process = None

    def start_process():
        nonlocal process
        process = multiprocessing.Process(target=local_main)
        process.start()

    def stop_process():
        if process:
            process.terminate()
            with open(__file__) as fd:
                pyperclip.copy(fd.read())

    class event_handler(FileSystemEventHandler):
        def on_modified(self, event):
            stop_process()
            logger.info("Changed: %s", event.src_path)
            start_process()

    dir_name = os.path.dirname(__file__)

    start_process()
    observer = Observer()
    observer.schedule(event_handler(), dir_name)
    observer.start()
    observer.join()


if __name__ == "__main__":
    if os.environ.get("LOCAL"):
        local__entry()
    else:
        main()
