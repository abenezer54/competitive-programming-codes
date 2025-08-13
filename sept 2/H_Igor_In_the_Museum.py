import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m, k = IL()
    grid = [S() for _ in range(n)]
    a = [IL() for _ in range(k)]
    ans = defaultdict(int)
    vis = [[0] * m for _ in range(n)]

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def inbound(i, j): return 0 <= i < n and 0 <= j < m
    col = 1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "." and vis[i][j] == 0:
                vis[i][j] = col
                walls = 0
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for side in range(len(d)):
                        r, c = d[side][0], d[side][1]
                        ni, nj = x + r, y + c
                        if inbound(ni, nj):
                            if grid[ni][nj] == "*":
                                walls += 1
                            elif vis[ni][nj] == 0:
                                stack.append((ni, nj))
                                vis[ni][nj] = col
                ans[col] = walls
                col += 1
    for x, y in a:
        col = vis[x - 1][y - 1]
        print(ans[col], end="\n")


solve()
