import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = [IL() for _ in range(n)]
    a.sort()
    def check(mid):
        d = mid * a[0][1]
        right = a[0][0] + d
        for i in range(1, n):
            d = mid * a[i][1]
            if a[i][0] - d > right:
                return False
            right = min(right, a[i][0] + d)
        return True
    
    l, r = 0, 1e10
    while l + 1e-8 < r:
        mid = round((l + r) / 2, 8)
        if check(mid):
            r = mid
        else:
            l = mid
    print(r)
solve()
