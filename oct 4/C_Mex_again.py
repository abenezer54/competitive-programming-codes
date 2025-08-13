import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = sorted(IL())
    idx = 0
    for num in range(1, n + 1):
        while idx < n and num > a[idx]:
            idx += 1
        # print(num, idx)
        if idx == n:
            print(num)
            return
        idx += 1
    print(n + 1)


solve()
