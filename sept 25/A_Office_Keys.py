import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
print(1 % 1)
def solve():
    n, k, p = IL()
    a = sorted(IL())
    b = sorted(IL())
    dp1 = [-1] * k
    mn = float('inf')
    for j in range(k):
        val = abs(a[0] - b[j]) + abs(b[j] - p)
        dp1[j] = val
        dp1[j] = min(mn, dp1[j])
        mn = min(mn, dp1[j])


    for i in range(1, n):
        dp2 = [-1] * k
        for j in range(i, k):
            prev_mn = dp1[j - 1]
            cur = abs(a[i] - b[j]) + abs(b[j] - p)
            dp2[j] = max(cur, prev_mn)
        dp1 = dp2
    print(min(dp1[n - 1:]))
        

solve()
