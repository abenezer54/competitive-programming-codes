import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = IL()
    c = Counter(a)
    ans = -1
    val = float("inf")
    for i in range(n):
        if c[a[i]] == 1:
            if a[i] < val:
                val = a[i]
                ans = i + 1
    print(ans)

for _ in range(II()):
    solve()
