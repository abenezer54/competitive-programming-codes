import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = IL()
    if len(set(a)) == 1:
        print(0)
        return

    g = []
    for i in range(n // 2):
        g.append(abs(a[i] - a[n - i - 1]))
    print(gcd(*g))



for _ in range(II()):
    solve()
