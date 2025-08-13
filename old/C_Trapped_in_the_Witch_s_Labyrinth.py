import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    grid = [S() for _ in range(n)]
    # print(grid)
    def inbound(i, j): return 0 <= i < n and 0 <= j < m 
    def change(i, j):
        if grid[i][j] == "R":
            return (i, j + 1)
        elif grid[i][j] == 'L':
            return (i, j - 1)
        elif grid[i][j] == 'U':
            return(i - 1, j)
        elif grid[i][j] == 'D':
            return (i + 1, j)
    

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    stack = []
    vis = [[0] * m for _ in range(n)]
   
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '?':
                x, y = change(i, j)
                if not inbound(x, y):
                    stack.append((i, j))
                    vis[i][j] = 1
    
    while stack:
        i, j = stack.pop()

        for k in range(4):
            ni, nj = i + d[k][0], j + d[k][1]
            if inbound(ni, nj) and vis[ni][nj] == 0:
                if k == 0:
                    if grid[ni][nj] == 'L':
                        vis[ni][nj] = 1
                        stack.append((ni, nj))
                elif k == 1:
                    if grid[ni][nj] == 'R':
                        vis[ni][nj] = 1
                        stack.append((ni, nj))
                elif k == 2:
                    if grid[ni][nj] == 'U':
                        vis[ni][nj] = 1
                        stack.append((ni, nj))
                else:
                    if grid[ni][nj] == 'D':
                        vis[ni][nj] = 1
                        stack.append((ni, nj))
    
    # ans = [[0] * m for _ in range(n)]
    # stack = []
    # print(vis)
    ans = 0
    for i in range(n):
        for j in range(m):
            if vis[i][j] == 0:
                if grid[i][j] != '?':
                    ans += 1
                else:
                    for k in range(4):
                        ni, nj = i + d[k][0], j + d[k][1]
                        if inbound(ni, nj) and vis[ni][nj] == 0:
                            ans += 1
                            break
    print(ans)
                

                    


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()