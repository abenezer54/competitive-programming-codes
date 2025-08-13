import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    left, right, d = IL()
    if left > d or right < d:
        print(d)
        return

    m = right % d
    if m == 0:
        m = d
    else:
        m = d - m
    print(right + m)
    

for _ in range(II()):
    solve()
