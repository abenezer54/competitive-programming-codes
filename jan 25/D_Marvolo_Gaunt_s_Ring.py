import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, p, q, r = IL()
    a = IL()
    dp = [[-float('inf')] * 3 for _ in range(n)]
    dp[0][0] = p * a[0]
    dp[0][1] = dp[0][0] + (q * a[0])
    dp[0][2] = dp[0][1] + (r * a[0])
    for i in range(1, n):
        for j in range(3):
            if j == 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j], a[i] * p)
            elif j == 1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1] + (q * a[i]))
            elif j == 2:
                dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1] + (r * a[i]))
                
    ans = -float('inf')
    for i in range(n):
        ans = max(ans, dp[i][2])
    print(ans)

tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()