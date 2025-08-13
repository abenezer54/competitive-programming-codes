import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    a = IL()
    dp = [[float('inf')] * (k + 1) for _ in range(n)]
    dp[0][0] = a[0]
    for i in range(n):
        for j in range(k + 1):
            if i == 0 and j == 0:
                continue
            
            for cur in range(min(i + 1, j + 1)):
                if cur == i:
                    mn = min(a[:i + 1])
                    dp[i][j] = min(dp[i][j], mn * (i + 1))
                else:
                    mn = min(a[i - cur:i + 1])
                    dp[i][j] = min(dp[i][j], dp[i - (cur + 1)][j - cur] + (mn * (cur + 1)))
    print(min(dp[-1]))



tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()