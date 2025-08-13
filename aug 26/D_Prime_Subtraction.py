import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    x, y = IL()
    d = x - y
    if d == 1:
        print("NO")
    else:
        print("YES")

for _ in range(II()):
    solve()
