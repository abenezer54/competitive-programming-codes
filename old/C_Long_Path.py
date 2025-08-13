import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = [0] + IL()
    dp = [0] * (n + 2)
    dp[1] = 2
    mod = int(1e9) + 7

    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + 2)  % mod
        dp[i] += (dp[i - 1] - dp[a[i] - 1]) % mod
        dp[i] %= mod
        
    print(dp[n])

tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()