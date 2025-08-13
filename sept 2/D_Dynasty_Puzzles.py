import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = [S() for _ in range(n)]
    dp = [[-1] * 26 for _ in range(26)]
    for word in a:
        start_idx = ord(word[0]) - 97
        end_idx = ord(word[-1]) - 97
        for i in range(26):
            if dp[i][start_idx] != -1:
                dp[i][end_idx] = max(dp[i][end_idx], dp[i][start_idx] + len(word))
        dp[start_idx][end_idx] = max(dp[start_idx][end_idx], len(word))
    ans = 0
    for i in range(26):
        for j in range(26):
            if dp[i][j] != -1 and i == j:
                ans = max(ans, dp[i][j])
    print(ans)
solve()
