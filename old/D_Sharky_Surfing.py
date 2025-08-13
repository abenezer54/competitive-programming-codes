import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m, L = IL()
    hurdles = []
    for _ in range(n):
        hurdles.append(IL())
    power_up = []
    for _ in range(m):
        power_up.append(IL()) 
    
    wait = []
    sm = 1
    idx = 0
    ans = 0
    for l, r in hurdles:
        while idx < m and power_up[idx][0] < l:
            heappush(wait, -power_up[idx][1])
            idx += 1
        need = r - l + 2
        while sm < need and wait:
            val = -heappop(wait)
            sm += val
            ans += 1
        if sm < need:
            print(-1)
            return
    print(ans)




tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()