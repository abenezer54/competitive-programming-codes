import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    k = II()
    n = II()
    a = [II() for _ in range(n)]
    def check(mid):
        tot = 0
        for i in range(n):
            tot += min(mid, a[i])
        return tot >= mid * k

    l, r = 0, int(1e11)
    while l + 1 < r:
        mid = (l + r) // 2
        if check(mid):
            l = mid
        else:
            r = mid
    print(l) 
solve()
