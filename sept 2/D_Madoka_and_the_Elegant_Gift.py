import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    grid = [S() for _ in range(n)]
    # print(grid)
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def inbound(i, j): return (0 <= i < n) and (0 <= j < m)
    vis = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1' and (i, j) not in vis:
                vis.add((i, j))
                stack = [(i, j)]
                l, r, t, b = float('inf'), -1, float('inf'), -1
                while stack:
                    x, y = stack.pop()
                    # print('node', x, y)
                    l = min(l, y)
                    r = max(r, y)
                    t = min(t, x)
                    b = max(b, x)

                    for d1, d2 in d:
                        ni, nj = x + d1, y + d2
                        if inbound(ni, nj) and ((ni, nj) not in vis) and grid[ni][nj] == '1':
                            stack.append((ni, nj))
                            vis.add((ni, nj))
                # print(t, b)
                # print('right', l, r)
                for k in range(t, b + 1):
                    for q in range(l, r + 1):
                        if grid[k][q] == '0':
                            print("NO")
                            return
    print("YES")                



for _ in range(II()):
    solve()
