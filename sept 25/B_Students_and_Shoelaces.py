import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    adj = [[] for _ in range(n + 1)]
    ind = [0] * (n + 1)
    for _ in range(m):
        x, y = IL()
        adj[x].append(y)
        adj[y].append(x)
        ind[x] += 1
        ind[y] += 1
    vis = [0] * (n + 1)
    ans = 0
    while True:
        arr = []
        for node in range(1, n + 1):
            if ind[node] == 1 and vis[node] == 0:
                arr.append(node)
                vis[node] = 1
        if not arr:
            break
        ans += 1

        for node in arr:
            for nei in adj[node]:
                ind[nei] -= 1
            
    print(ans)
    
    

solve()
