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
    adj = [[] for _ in range(n + 1)]
    childs = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        x, y = IL()
        adj[x].append(y)
        adj[y].append(x)
    

    vals = defaultdict(lambda: defaultdict(int))
    tot = defaultdict(int)
    parent = defaultdict(int)
    stack = [1]
    vis = set(stack)
    while stack:
        node = stack[-1]
        for nei in adj[node]:
            if nei not in vis:
                stack.append(nei)
                parent[nei] = node
                vis.add(nei)
        
        if node == stack[-1]:
            stack.pop()
            tot[node] += a[node - 1]
            if a[node - 1] == 0:
                tot[node] -= 1
            tot[node] = max(tot[node], 0)
            if node != 1:
                tot[parent[node]] += tot[node]
                vals[parent[node]][node] = tot[node]

    ans = [0] * n
    stack = [1]
    vis = set(stack)
    while stack:
        node = stack.pop()
        tot = 1 if a[node - 1] == 1 else -1

        for val in vals[node].values():
            tot += val

        ans[node - 1] = tot
        
        for nei in adj[node]:
            if nei not in vis:
                vals[nei][node] = max(0, tot - vals[node][nei])
                stack.append(nei)
                vis.add(nei)
    
    print(*ans)       
            

solve()
