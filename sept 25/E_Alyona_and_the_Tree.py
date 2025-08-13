import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = [0] + IL()
    adj = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        p, c = IL()
        # adj[i + 2].append((p, c))
        adj[p].append((i + 2, c))
    # print(adj)
    if n == 1:
        print(0)
        return
    
    childs = [0] * (n + 1)
    stack = [1]
    parent = [-1] * (n + 1)
    vis = [0] * (n + 1)
    vis[1] = 1
    while stack:
        # print(stack)
        node = stack[-1]
        for nei, _ in adj[node]:
            if vis[nei] != 1:
                parent[nei] = node
                stack.append(nei)
                vis[nei] = 1

        if node == stack[-1]:
            
            node = stack.pop()
            prt = parent[node]
            if prt != -1:
                childs[prt] += childs[node] + 1
    
    stack = [(1, 0)]
    ans = 0
    while stack:
        node, prev = stack.pop()
        if prev > a[node]:
            ans += childs[node] + 1
        else:
            for nei, w in adj[node]:
                x = prev + w
                x = max(0, x)
                stack.append((nei, x))
    print(ans)

solve()
