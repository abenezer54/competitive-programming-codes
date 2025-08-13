import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    a = IL()
    tot = ((n - 1) * 2) + n
    prev = set()
    s = set()
    # print(tot)
    for i in range(k):
        if a[i] - 1 in prev:
            s.add((a[i] - 1, a[i]))
        if a[i] + 1 in prev:
            s.add((a[i] + 1, a[i]))  
        prev.add(a[i])
    print(tot - len(prev) - len(s))


solve()
