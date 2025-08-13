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
    dp = [defaultdict(list) for _ in range(n)]
    val1 = (0, a[0][1] / 2, 0)
    val2 = (a[0][0] - a[0][1], 0, a[0][1])
    dp[0][0].append(val1)
    dp[0][1].append(val2)
    
    for i in range(1, n):
        for j in range(i + 1):
            for space, remain, val  in dp[i - 1][j]:
                # use the current
                ns = space +( a[i][0] - a[i][1])
                nr = remain
                rr = min(ns, nr)
                nr -= rr
                ns -= rr
                nv = val + a[i][1] + rr
                dp[i][j + 1].append((ns, nr, nv))

                # do not use the current
                half = a[i][1] / 2
                useable = half if space >= half else space
                ns = space - useable
                nr = remain + (half - useable)
                nv = val + useable
                dp[i][j].append((ns, nr, nv))
    ans = [0] * n
    for i in range(n):
        for j in range(i + 2):
            for val in dp[i][j]:
                if j > 0:
                    ans[j - 1] = max(ans[j - 1], val[-1])
    print(*ans)


                
solve()
