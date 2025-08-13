import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = IL()
        adj[x].append(y)
        adj[y].append(x)
    
    vis = [0] * (n + 1)
    tin = [-1] * (n + 1)
    low = [-1] * (n + 1)
    size = [1] * (n + 1)
    parent = list(range(n + 1))
    time = 0
    stack = [1]
    ans = ((n * (n - 1)) // 2)
    while stack:
        node = stack[-1]
        if vis[node] == 0:
            tin[node] = low[node] = time
            vis[node] = 1
            time += 1
        
        for nei in adj[node]:
            if vis[nei] == 0:
                stack.append(nei)
                parent[nei] = node
        
        if node == stack[-1]:

            node = stack.pop()
            mn, par = float('inf'), -1

            for nei in adj[node]:
                if parent[node] == nei:
                    par = nei
                else:
                    mn = min(mn, low[nei])

            if par != -1:
                if mn > tin[par]:
                    val = size[node]
                    val2 = n - size[node]
                    ans = min(ans, ((n * (n - 1)) // 2) - (val * val2))
                    low[node] = min(low[node], mn, tin[par])
                else:
                    low[node] = min(low[node], mn)
                    
            size[par] += size[node]

    print(ans)


for _ in range(II()):
    solve()
