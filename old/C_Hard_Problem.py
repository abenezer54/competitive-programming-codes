import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    m, a, b, c = IL()
    tot = 2 * m
    tot -= min(m, a)
    tot -= min(m, b)
    if tot > 0:
        tot = max(0, tot - c)
    print((2 * m) - tot)
    


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()