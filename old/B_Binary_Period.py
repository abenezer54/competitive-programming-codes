import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    s = S()
    n = len(s)
    cnt = Counter(s)
    if len(cnt) == 1:
        print(s)
        return
    for length in range(2, n):
        


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()