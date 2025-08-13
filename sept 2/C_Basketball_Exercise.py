import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = IL()
    b = IL()
    dp = [[0] * 3 for _ in range(n)]
    # print(dp)
    dp[0][1] = a[0]
    dp[0][2] = b[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i][0], dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = a[i] + max(dp[i][1], dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = b[i] + max(dp[i][2], dp[i - 1][0], dp[i - 1][1])
    print(max(dp[-1]))


solve()
