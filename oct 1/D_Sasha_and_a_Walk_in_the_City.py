import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
MOD = 998244353
def solve():
    n = II()
    adj = defaultdict(list)
    for _ in range(n - 1):
        u, v = IL()
        adj[u].append(v)
        adj[v].append(u)
    stack = []
    tot = pow(2, n, MOD)
    idk = 0
    for node in range(1, n + 1):
        cnt = len(adj[node])
        cur = n - cnt - 1
        idk += pow(2, cur) - 1
        # print(node, adj[node], pow(2, cur))
    tot -= idk //2
    print(tot )


for _ in range(II()):
    solve()
