import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    INF = -int(1e9)
    dp = [INF] * 5
    dp[-1] = 0
    narek = 'narek'
    for _ in range(n):
        s = S()
        cnt = 0
        for j in range(m):
            if s[j] in narek:
                cnt += 1

        temp = dp[:]

        for start in range(5):
            res = dp[start - 1] - cnt
            cur = start
            for j in range(m):
                if s[j] == narek[cur % 5]:
                    if cur % 5 == 4:
                        res += 10
                    temp[cur % 5] = max(temp[cur % 5], res)
                    cur += 1
        dp = temp
    print(dp[-1])

for _ in range(II()):
    solve()
