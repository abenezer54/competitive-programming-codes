import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = IL()
    mn = float('inf')
    x, y = -1, -1
    for i in range(n - 1):
        diff = abs(a[i + 1] - a[i])
        if diff < mn:
            mn = diff
            x = i + 1
            y = i + 2
    if abs(a[-1] - a[0]) < mn:
        x = n
        y = 1
    print(x, y)

tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()