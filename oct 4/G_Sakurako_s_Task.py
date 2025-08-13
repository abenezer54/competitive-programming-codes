import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    a = IL()
    gcd = math.gcd(*a)
    if n == 1:
        if a[0] < k:
            print(k)
        else:
            print(k - 1) 
    else:
        cnt = (n - 1) * (gcd - 1)
        mx = (n - 1) * gcd
        if k <= cnt:
            p = math.ceil(k / (gcd - 1)) - 1
            r = k % (gcd - 1)
            if r == 0:
                r = gcd - 1
            ans = (gcd * p) + r
            print(ans)
        else:
            print(mx + (k - cnt))

for _ in range(II()):
    solve()
