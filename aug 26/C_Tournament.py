import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

# print(log2(1e4))
def solve():
    n, k = IL()
    a = IL()
    dp = [[0] * 15 for _ in range(n)]
    for i in range(min(n, 15)):
        val = a[-1] // pow(2, i)
        dp[-1][i] = max(val - k, val // 2)

    for i in range(n - 2, -1, -1):
        for j in range(min(i + 1, 14)):
            val = a[i] // pow(2, j)
            x = val - k + dp[i + 1][j] 
            y = (val // 2) + dp[i + 1][j + 1]
            dp[i][j] = max(x, y)
    print(dp[0][0])
for _ in range(II()):
    solve()
