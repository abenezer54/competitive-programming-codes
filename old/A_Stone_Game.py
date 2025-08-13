import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = IL()
    idx = a.index(max(a))
    idx2 = a.index(min(a))
    mn = min(idx, idx2)
    mx = max(idx2, idx) 
    x = mx - mn + 1 + min(mn, n - mx - 1)
    y = mn + 1 + (n - mx)
    print(min(x, y))


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()