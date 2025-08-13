import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    s = S()
    t = []
    for i in range(n):
        if t and t[-1] == s[i]:
            continue
        t.append(s[i])
    dp = [[0] * 505 for _ in range(505)]
    def calc_dp(l, r):
        if l == r:
            dp[l][r] = 1
            return 1
        if dp[l][r]:
            return dp[l][r]

        dp[l][r] = 1 + calc_dp(l, r - 1)
        for j in range(r - 1, l - 1, -1):
            if t[j] == t[r]:
                dp[l][r] = min(dp[l][r], calc_dp(l, j) + calc_dp(j + 1, r - 1))
        return dp[l][r]
    
    print(calc_dp(0, len(t) - 1))

solve()
