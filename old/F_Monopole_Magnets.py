import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    grid = [S() for _ in range(n)]
    rmx = [[float('inf'), -float("inf")] for _ in range(n)]
    cmx = [[float('inf'), -float("inf")] for _ in range(m)]
    row = [False] * n
    col = [False] * m
    # print(grid)
    found = False
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                row[i] = True
                col[j] = True
                found = True
                rmx[i][0] = min(rmx[i][0], j)
                rmx[i][1] = max(rmx[i][1], j)
                cmx[j][0] = min(cmx[j][0], i)
                cmx[j][1] = max(cmx[j][1], i)

    for i in range(n):
        for j in range(m):
            # print(i, j)
            if grid[i][j] == '.' and (rmx[i][0] <=  j <= rmx[i][1] or cmx[j][0] <= i <= cmx[j][1]):
                print(-1)
                return

    if (False in row and False not in col) and found:
        print(-1)
        return 
    if (False in col and False not in row) and found:
        print(-1)
        return 
    
    ans = 0
    vis = [[0] * m for _ in range(n)]
    def inbound(i, j): return 0 <= i < n and 0 <= j < m
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(n):
        for j in range(m):
            if vis[i][j] == 0 and grid[i][j] == '#':
                # print(i, j)
                ans += 1
                stack = [(i, j)]
                vis[i][j] = 1

                while stack:
                    x, y = stack.pop()
                    for r, c in d:
                        ni, nj = x + r, y + c
                        if inbound(ni, nj) and vis[ni][nj] == 0 and grid[ni][nj] == '#':
                            stack.append((ni, nj))
                            vis[ni][nj] = 1
    print(ans)


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()