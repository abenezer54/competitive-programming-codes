import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    grid = []
    for _ in range(n):
        grid.append(IL())
    check = set()
    idx = defaultdict()
    for j in range(n):
        check.add(grid[j][0])
        idx[grid[j][0]] = j
    ans = defaultdict(int)
    for _ in range(m):
        row = IL()
        if set(row) == check:
            for i, val in enumerate(row):
                ans[idx[val]] = i
    res = [[-1] * m for _ in range(n)]
    for i in range(n):
        res[ans[i]] = grid[i].copy()
    for row in res:
        print(*row)


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()