import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    grid = [S() for _ in range(n)]
    vis = [[False] * m for _ in range(n)]
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def inbound(i, j): return 0 <= i < n and 0 <= j < m
    parent =[[-1] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                que = deque([(i, j)])
                while que:
                    x, y = que.popleft()
                    if grid[x][y] == 'B':
                        print("YES")
                        path = []
                        while parent[x][y] != -1:
                            w, z = parent[x][y]
                            d1, d2 = w - x, z - y
                            if d1 == 0 and d2 == 1:
                                path.append('L')
                            elif d1 == 0 and d2 == -1:
                                path.append("R")
                            elif d1 == 1 and d2 == 0:
                                path.append("U")
                            else:
                                path.append("D")
                            x, y = w, z
                        print(len(path))
                        print("".join(path[::-1]))
                        return 

                    for r, c in d:
                        ni, nj = x + r, y + c
                        if inbound(ni, nj) and grid[ni][nj] in ['.', 'B'] and not vis[ni][nj]:
                            que.append((ni, nj))
                            parent[ni][nj] = (x, y)
                            vis[ni][nj] = True
                            
    print("NO")


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()