import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = [IL() for _ in range(n)]
    dp = [defaultdict(int) for _ in range(n)]
    dp[0][a[0][0]] = 0
    dp[0][a[0][0] + 1] = a[0][1]
    dp[0][a[0][0] + 2] = 2 * a[0][1]

    for i in range(1, n):
        cur = [float("inf")] * 3
        for k, v in dp[i - 1].items():
            for j in range(3):
                if k != a[i][0] + j:
                    cur[j] = min(cur[j], v)
        cur[1] += a[i][1]
        cur[2] += 2 * a[i][1]
        for j in range(3):
            dp[i][a[i][0] + j] = cur[j]
    print(min(dp[-1].values()))

for _ in range(II()):
    solve()
