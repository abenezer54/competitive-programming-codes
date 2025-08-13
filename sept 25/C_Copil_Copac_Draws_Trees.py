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
    edge_idx = defaultdict(int)
    for idx in range(n - 1):
        x, y = IL()
        edge_idx[(x, y)] = idx
        edge_idx[(y, x)] = idx
        adj[x].append(y)
        adj[y].append(x)
        
    vis = [0] * (n + 1)
    stack = [(1, -1, 0)]
    ans = 0
    while stack:
        node, prev, val = stack.pop()
        ans = max(ans, val)
        for nei in adj[node]:
            if vis[nei] == 0:
                nval = val
                vis[nei] = 1
                nxt = edge_idx[(node, nei)]
                if nxt < prev:
                    nval += 1
                stack.append((nei, nxt, nval))
    print(ans + 1)
        

    

for _ in range(II()):
    solve()
