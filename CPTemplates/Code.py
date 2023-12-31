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
    print(f"3 + 3 = {3 + 3}")


def main():
    if MULTIPLE_TESTS:
        for _ in range(int(input())):
            solve()
    else:
        solve()


if __name__ == "__main__":
    if os.environ.get("LOCAL"):
        from local import *
        local__entry(main, __file__)
    else:
        main()
