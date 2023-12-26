import os
import sys
import time
import heapq
import itertools
import functools

MULTIPLE_TESTS = True

def inp():
    return list(map(int, input().split(" ")))

def solve():
    n = int(input())
    if n in [1, 2, 5]:
        print("NO")
    else: print("YES")

def main():
    if MULTIPLE_TESTS:
        for _ in range(int(input())):
            solve()
    else: solve()


def local_main():
    sys.stdin = open("input.txt")
    main()


if __name__ == '__main__':
    if os.environ.get("LOCAL"):
        import logging
        import multiprocessing
        import pyperclip

        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger("Auto-Reload")

        lt = 0
        p = None

        while True:
            if os.path.getmtime(__file__) > lt:
                if p:
                    p.terminate()
                logger.info(
                    "Detected changes in %s | %s", __file__, time.asctime()
                )

                p = multiprocessing.Process(target=local_main, daemon=True)
                p.start()
                lt = os.path.getmtime(__file__)
                pyperclip.copy(open(__file__).read())

            time.sleep(1)
    else:
        main()
