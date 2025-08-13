import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    def check(mid):
        kk = k
        cur = mid
        p = 1
        while mid // pow(kk, p) != 0:
            cur += mid // pow(kk, p)
            p += 1
        return cur >= n

    l, r = 0, int(1e18)
    while l + 1 < r:
        mid = (l + r) // 2
        # print(mid, check(mid), l)
        if check(mid):
            r = mid
        else:
            l = mid
    print(r)

solve()
