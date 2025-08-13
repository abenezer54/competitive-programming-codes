import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    grid = [IL() for _ in range(n)]
    # print(grid)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j and  i == 0:
                continue
            dp[i][j] = max(dp[i-1][j] , dp[i][j - 1]) + grid[i - 1][j - 1]

    dp2 = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if i == j and i == n - 1:
                continue
            dp2[i][j + 1] = grid[i - 1][j - 1]  + max(dp2[i + 1][j + 1], dp2[i][j])
    print(dp)
    # print(dp2)
    ans = 0
    for i in range(n):
        for j in range(m):
            # taking the top
            val = dp[i][j + 1] + max(dp2[i][j], dp2[i + 1][j + 1])
            # taking the left
            val2 = dp[i][j]  + dp2[i + 1][j + 1]
            mx = max(val , val2)
            if i == j == 1:
                print(dp[i][j + 1])
            ans = max(ans, mx - grid[i][j])
    print(ans)
solve()
