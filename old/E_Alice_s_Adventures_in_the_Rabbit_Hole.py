import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def mod_inverse(q, M):
    return pow(q, -1, M)

def mod_divide(p, q, M):
    q_inv = mod_inverse(q, M)
    return (p * q_inv) % M

MOD =  998244353

def solve():
    n = IL()[0]
    adj = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        x, y = IL()
        adj[x].append(y)
        adj[y].append(x)
        
    stack = [(1, 0)]
    vis = [0] * (n + 1)
    vis[1] = 1
    mn_leaf = [float('inf')] * (n + 1)
    parent = [-1] * (n + 1)
    level = [0] * (n + 1)
    while stack:
        node, lvl = stack[-1]

        for nei in adj[node]:
            if vis[nei] == 0:
                stack.append((nei, lvl + 1))
                level[nei] = lvl + 1
                vis[nei] = 1
                parent[nei] = node
        
        

        if node == stack[-1][0]:
            node, lvl = stack.pop()
            if len(adj[node]) == 1 and node != 1:
                mn_leaf[node] = lvl
            for nei in adj[node]:
                if nei != parent[node]:
                    mn_leaf[node] = min(mn_leaf[node], mn_leaf[nei])

    ans = [1]
    for node in range(2, n + 1):
        p = level[node]
        q = mn_leaf[node] - level[node]
        if len(adj[node]) == 1:
            ans.append(0)
            continue
        ans.append(mod_divide(p, p + q, MOD))
    print(ans)       



tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()