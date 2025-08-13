import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    x = IL()[0]
    arr = []

    for i in range(int(1e18)):
        arr.extend([1] * 1000)
        for j in range(12):
            if x == j:
                continue
    
tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()