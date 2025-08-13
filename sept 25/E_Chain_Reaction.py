import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = [IL() for _ in range(n)]
    a.insert(0, [-1, 0])
    a.sort()
    # print(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        target = max(-1, a[i][0] - a[i][1] - 1)
        # print(target)
        l, r = 0, n + 1
        while l + 1 < r:
            mid = (l + r) // 2
            if a[mid][0] <= target:
                l = mid
            else:
                r = mid

        dp[i] = dp[l] + 1
    # print(dp)
    print(n - max(dp))
solve()
