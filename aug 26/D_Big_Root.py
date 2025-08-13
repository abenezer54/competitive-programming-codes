import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = IL()
    p = IL()
    ind = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for i in range(n  - 1):
        ind[p[i]] += 1
        adj[i + 2].append(p[i])
        
    mn = [float('inf')] * (n + 1)
    que = deque()
    for i in range(1, n + 1):
        if ind[i] == 0:
            que.append(i)
            mn[i] = a[i - 1]

    while que:
        node = que.pop()
        if node != 1 and a[node - 1] < mn[node]:
            mn[node] = (a[node - 1] + mn[node]) // 2

        for nei in adj[node]:
            mn[nei] = min(mn[nei], mn[node])
            
            ind[nei] -= 1
            if ind[nei] == 0:
                que.append(nei)
    print(mn[1] + a[0])

for _ in range(II()):
    solve()