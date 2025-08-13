import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a , b = 1, 0
    n -= 1
    mux = 1
    cnt = 0 
    for i in range(2, int(1e6)):
        val = min(n, i)
        if mux == 0:
            a += val
            cnt += 1
            if cnt == 2:
                mux = 1
                cnt = 0
        else:
            cnt += 1
            b += val
            if cnt == 2:
                mux = 0
                cnt = 0
        n -= val
        if n <= 0:
            break
    print(a, b)


for _ in range(II()):
    solve()
