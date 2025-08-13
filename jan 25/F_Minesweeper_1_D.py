import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    s = S()
    n = len(s)
    MOD = int(1e9) + 7
    dp = [[0] * 3 for _ in range(n + 5)]
    for i in range(n):
        if s[i] == '?':
            pass     

        elif s[i] == '*':
            # dp[i][2] += 1 
            dp[i][2] += dp[i - 1][1]
        elif s[i] == '1' or s[i] == '2':
            # dp[i][1] += 1
            dp[i][1] += dp[i - 1][2]
        elif s[i] == '0':
            # dp[i][0] += 1
            dp[i][0] += dp[i - 1][1]
        # elif s[i] == '2':





tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()