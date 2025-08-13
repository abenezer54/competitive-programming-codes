import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    grid = [S() for _ in range(n)]
    d = [(0, -1), (-1, 0)]
    def inbound(i, j): return (0 <= i < n) and (0 <= j < n)

    tot = 0
    for i in range(n):
        tot += grid[i].count("1")

    vis = set()
    que = deque()
    for i in range(n):
        if grid[i][n - 1] == "1":
            vis.add((i, n - 1))
            que.append((i, n - 1))
        if grid[n - 1][i] == '1':
            vis.add((n - 1, i))
            que.append((n - 1, i))
    
    while que:
        i, j = que.popleft()
        for x, y in d:
            ni, nj = i + x, j + y
            if inbound(ni, nj) and grid[ni][nj] == '1' and (ni, nj) not in vis:
                que.append((ni, nj))
                vis.add((ni, nj))

    if len(vis) < tot:
        print("NO")
    else:
        print("YES")
for _ in range(II()):
    solve()
