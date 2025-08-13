import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    grid = [S() for _ in range(n)]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] += dp[i][j]
            # if j > 0:
            for k in range(i):
                if j > 0 and grid[k][j] == '.' and grid[k][j - 1] == '.':
                    dp[i + 1][j + 1] += 1
                if k > 0:
                    if grid[k][j] == '.' and grid[k - 1][j] == '.':
                        dp[i + 1][j + 1] += 1
            # if i > 0:
            for k in range(j):
                if i > 0 and grid[i][k] == '.' and grid[i - 1][k] ==  '.':
                    dp[i + 1][j + 1] += 1
                if k > 0:
                    if grid[i][k] == '.' and grid[i][k - 1] == '.':
                        dp[i + 1][j + 1] += 1

            if j > 0 and grid[i][j] == '.' and grid[i][j - 1] == '.':
                dp[i + 1][j + 1] += 1
            if i > 0 and grid[i][j] == '.' and grid[i - 1][j] == '.':
                dp[i + 1][j + 1] += 1
    # print(dp)    
    q = IL()[0]
    for _ in range(q):
        r1, c1, r2, c2 = IL()
        # if r1 == 1 and c1 == 7:
        #     print('here', dp[r1 - 1][c1 - 1], dp[r2][c2], dp[r1 - 1][c2], dp[r2][c1 - 1])
        print(dp[r2][c2] + dp[r1 - 1][c1 - 1] - dp[r1 - 1][c2] - dp[r2][c1 - 1])


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()