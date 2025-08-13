import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, b, d = IL()
    a = IL()
    tot = 0
    ans = 0
    for i in range(n):
        if a[i] > b:
            continue
    
        tot += a[i]
        if tot > d:
            ans += 1
            tot = 0
    print(ans)


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()