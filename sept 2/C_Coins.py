import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(0, n + 1):
        if dp[i]:
            nxt = i + 3
            if nxt < len(dp):
                dp[nxt] = 1
    
    for i in range(n + 1):
        if dp[i]:
            nxt = i + 5
            if nxt < len(dp):
                dp[nxt] = 1
    # print(dp)
    for i in range(n, -1, -1):
        if dp[i]:
            print(n - i)
            return

for _ in range(II()):
    solve()
