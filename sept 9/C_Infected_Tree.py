import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    adj = [[] for _ in range(n + 1)]
    vis = [0] * (n + 1)
    for _ in range(n - 1):
        x, y = IL()
        adj[x].append(y)
        adj[y].append(x)

    parent = defaultdict(int)
    childs = defaultdict(int)
    stack = [1]
    vis[1] = 1
    dp = [0] * (n + 5)
    while stack:
        node = stack[-1]

        for nei in adj[node]:
            if vis[nei] == 0:
                stack.append(nei)
                vis[nei] = 1
                parent[nei] = node

        if node == stack[-1]:
            node = stack.pop()
            neighbors = []
            for nei in adj[node]:
                if nei != parent[node]:
                    neighbors.append(nei)
            if node != 1:
                if len(neighbors) == 0:
                    childs[parent[node]] += 1
                elif len(neighbors) == 1:
                    childs[parent[node]] += childs[node] + 1
                else:
                    childs[parent[node]] += childs[node] + 1

            if len(neighbors) == 0:
                dp[node] = max(dp[node], 0)
            elif len(neighbors) == 1:
                dp[node] = max(dp[node], childs[neighbors[0]])
            else:
                val1 = childs[neighbors[1]] + dp[neighbors[0]]
                val2 = childs[neighbors[0]] + dp[neighbors[1]]
                dp[node] = max(dp[node], val1, val2)

    print(dp[1])


for _ in range(II()):
    solve()
