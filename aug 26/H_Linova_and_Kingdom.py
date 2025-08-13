import sys
import heapq
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k  = IL()
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = IL()
        adj[v].append(u)
        adj[u].append(v)

    childs = [0] * (n + 1)
    stack = [1]
    vis = set([1])
    cnt = 0
    parent = {}
    while stack:
        node = stack[-1]
        flag = False
        for nei in adj[node]:
            if nei not in vis:
                flag = True
                stack.append(nei)
                vis.add(nei)
                parent[nei] = node
        
        if not flag:
            node = stack.pop()
            if node != 1:
                p = parent[node]
                childs[p] += childs[node] + 1

    que = deque([(1, 0)])
    vis = set([1])
    arr = []
    while que:
        node, d = que.popleft()
        cnt = 0
        for nei in adj[node]:
            if not nei in vis:
                vis.add(nei)
                cnt += 1
                que.append((nei, d + 1))
        arr.append(d - childs[node])
    arr.sort(reverse=True)
    ans = 0
    for i in range(k):
        ans += arr[i]
    print(ans)



solve()
