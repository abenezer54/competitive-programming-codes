import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    h = 0
    cur = 1
    while n > 0:
        n -= (cur * (cur + 1)) // 2
        # print(n, (cur * (cur + 1)) // 2)
        cur += 1   
        h += 1
        if n < 0:
            h -= 1
    print(h)


solve()
