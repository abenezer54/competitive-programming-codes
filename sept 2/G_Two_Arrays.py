import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m  = IL()
    dpa = [[0] * (n + 1) for _ in range(m)]
    for i in range(1, n + 1):
        dpa[0][i] = 1  
    for i in range(1, m):
        for j in range(1, n + 1):
            for k in range(1, j + 1):
                dpa[i][j] += dpa[i - 1][k]

    
    dpb = [[0] * (n + 1) for _ in range(m)]
    for i in range(1, n + 1):
        dpb[0][i] = 1  

    for i in range(1, m):
        for j in range(1, n + 1):
            for k in range(j, n + 1):
                dpb[i][j] += dpb[i - 1][k]
    MOD = pow(10, 9) + 7
    ans  = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            ans  += (dpa[-1][i] * dpb[-1][j]) % MOD

    print(ans % MOD)


solve()
