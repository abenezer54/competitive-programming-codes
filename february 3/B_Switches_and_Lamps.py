import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    grid = [S() for _ in range(n)]
    cnt = [0] * m
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                cnt[j] += 1
    for i in range(n):
        found = False
        for j in range(m):
            if grid[i][j] == '1' and cnt[j] == 1:
                found = True
        if not found:
            print("YES")
            return
    print("NO")
        


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()