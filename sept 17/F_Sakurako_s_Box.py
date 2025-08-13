import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = IL()
    mod = int(1e9) + 7
    p =  a[:]
    for i in range(1, len(p)):
        p[i] += p[i - 1]

    tot = 0
    pair = 0
    for i in range(n):
        cur = a[i] * (p[n - 1] - p[i]) 
        # print(cur, a[i], p[n - 1] - p[i])
        tot += cur
        pair += n - i - 1
        cur %= mod
    print(((tot % mod ) * (pow(pair, -1, mod))) % mod)

    

for _ in range(II()):
    solve()
