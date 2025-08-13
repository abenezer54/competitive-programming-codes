import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    adj = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        x, y = IL()
        adj[x].append(y)
        adj[y].append(x)

    childs = [0] * (n + 1)
    mx_level = [0] * n
    stack = [(1, 0)]
    parent = [-1] * (n + 1)
    count = [0] * (n + 1)
    while stack:
        node, lvl = stack[-1]
        if len(adj[node]) == 1 and node != 1:
            mx_level[node - 1] = lvl
        for nei in adj[node]:
            if parent[nei] == -1 and nei != 1:
                parent[nei] = node
                stack.append((nei, lvl + 1))


        if node == stack[-1][0]:  
            node, lvl = stack.pop()
            count[mx_level[node - 1]] += 1
            prt = parent[node]
            if prt != -1:
                childs[prt] += childs[node] + 1
                mx_level[prt - 1] = max(mx_level[prt - 1], mx_level[node - 1])

    vis = [0] * (n + 1)
    vis[1] = 1
    que = deque([1])
    level = x = 0
    ans = float('inf')
    while que:
        ln = len(que)
        cur_level_childs = 0
        for _ in range(ln):
            node = que.popleft()
            cur_level_childs += childs[node]
            for nei in adj[node]:
                if vis[nei] == 0:
                    que.append(nei)
                    vis[nei] = 1
        ans = min(ans, cur_level_childs + x)
        x += count[level]
        level += 1

    print(ans)

for _ in range(II()):
    solve()
