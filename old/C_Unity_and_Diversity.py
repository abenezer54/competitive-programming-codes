import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()

    print(max(n, m) - 1, min(n, m))
    

tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()