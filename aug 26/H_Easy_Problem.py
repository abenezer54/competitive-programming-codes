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
    a = IL()
    dp = [0] * 4
    for i in range(n):
        if s[i] == 'h':
            dp[0] += a[i]
        elif s[i] == 'a':
            dp[1] = min(dp[0], dp[1] + a[i])
        elif s[i] == 'r':
            dp[2] = min(dp[1], dp[2] + a[i])
        elif s[i] == 'd':
            dp[3] = min(dp[2], dp[3] + a[i])
    print(dp[-1])


solve()
