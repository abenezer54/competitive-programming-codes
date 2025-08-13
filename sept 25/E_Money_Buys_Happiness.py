import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    m, x = IL()
    p = [IL() for _ in range(m)]
    mx = max(p, key=lambda x: x[1])[1]
    dp = [-1] * ((mx * m) + 5)
    dp[0] = 0
    for c, h in p:
        for j in range(len(dp) - 1, -1, -1):
            if dp[j] != -1 and dp[j] >= c:
                nxt = j + h
                if nxt < len(dp):
                    if dp[nxt] == -1:
                        dp[nxt] = dp[j] - c + x
                    else:
                        dp[nxt] = max(dp[nxt], dp[j] - c + x)
            if dp[j] != -1:
                dp[j] += x
    ans = 0
    for i in range(len(dp)):
        if dp[i] != -1:
            ans = i
    print(ans)



for _ in range(II()):
    solve()
