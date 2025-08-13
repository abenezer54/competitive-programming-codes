import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    m, n = IL()
    s = IL()
    l = IL()
    tot = [s[i] + l[i] for i in range(m)]
    mod = pow(10, 9) + 7
    dp = [[0 for _ in range(m)] for _ in range(n + 1)]
    dp[0][0] = 1
    
    def calc(i, j):
        val1 = l[i] * s[j]
        val2 = s[i] * tot[j]
        return val1 + val2
    

    for d in range(1, n + 1):
        for i in range(m):
            for j in range(m):
                dp[d][i] += dp[d - 1][j] * calc(j, i)
                dp[d][i] %= mod
    print(sum(dp[-1]) % mod)

solve()
