import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def calc(n):
    while len(str(n)) != 1:
        val = 1
        for digit in str(n):
            if digit != '0':
                val *= int(digit)
        n = int(val)
    return n

dp = [[0] * 10 for _ in range(1000005)]
for n in range(1, 1000005):
    val = calc(n)
    for j in range(10):
        dp[n][j] += dp[n - 1][j]
        if j == val:
            dp[n][j] += 1


def solve():
    l, r, k = IL()
    print(dp[r][k] - dp[l - 1][k])

for _ in range(II()):
    solve()
