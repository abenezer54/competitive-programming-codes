import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return float(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    c = II()
    def check(mid):
        val = pow(mid, 2) + math.sqrt(mid)
        return val <= c
        
    l, r = 1, int(1e6)
    while l + 1e-6 < r:
        mid = (l + r) / 2
        if check(mid):
            l = mid
        else:
            r = mid
    print(l)
    

solve()
