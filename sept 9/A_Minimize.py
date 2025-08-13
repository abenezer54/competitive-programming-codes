import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    a, b = IL()
    mn = float('inf')
    for i in range(a, b + 1):
        cur = (i - a) + (b - i)
        if cur < mn:
            mn = cur
    print(mn)

for _ in range(II()):
    solve()
