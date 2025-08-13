import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
#nx, ny = x + d[1][0], y + d[1][1]
def solve():
    n, m, k = IL()
    grid = [S() for _ in range(n)]
    def inbound(i, j): return (0 <= i < n) and (0 <= j < m)
    d = [(-1, -1), (-1, 1)]
    tot = set()
    
    for i in range(n):
        for j in range(m):
            # print(i, j)
            if grid[i][j] == "*" :
                stack = [(i, j, 0)]
                path1 = deque([(i, j, 0)])
                mx1 = 0
                while stack:
                    x, y, length = stack.pop()
                    ni, nj = x + d[0][0], y + d[0][1]
                    mx1 = max(mx1, length)
                    if inbound(ni, nj)  and grid[ni][nj] == "*":
                        path1.append((ni, nj, length + 1))
                        stack.append((ni, nj, length + 1))
                
                stack = [(i, j, 0)]
                path2 = deque([(i, j, 0)])
                mx2 = 0
                while stack:
                    x, y, length = stack.pop()
                    ni, nj = x + d[1][0], y + d[1][1]
                    mx2 = max(mx2, length)
                    if inbound(ni, nj)  and grid[ni][nj] == "*" :
                        path2.append((ni, nj, length + 1))
                        stack.append((ni, nj, length + 1))
                # print('here', mx1, mx2)
                # print(path1)
                mn = min(mx1, mx2)
                if mn >= k:
                    while path1 and path1[0][2] <= mn :
                        x = path1.popleft()
                        tot.add((x[0], x[1]))
                    while path2 and path2[0][2] <= mn :
                        x = path2.popleft()
                        tot.add((x[0], x[1]))

    tott = 0
    for row in grid:
        tott += row.count('*')

    if len(tot) == tott:
        print("YES")
    else:
        print("NO")
                
                









for _ in range(II()):
    solve()
