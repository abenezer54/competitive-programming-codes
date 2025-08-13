import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    a, b = IL()
    d = abs(a - b)
    if d == 0:
        print(0, 0)
        return
    print(d, min(a % d, d - (a % d)))

for _ in range(II()):
    solve()
