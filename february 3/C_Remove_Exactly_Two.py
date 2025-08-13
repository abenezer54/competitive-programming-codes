import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    ind = [0] * (n + 1)
    for _ in range(n - 1):
        x, y = IL()
        adj[x].append(y)
        adj[y].append(x)
        degree[x] += 1
        degree[y] += 1
        ind[x] += 1
        ind[y] += 1

    que = deque()
    for node in range(1, n + 1):
        if degree[node] == 1:
            que.append(node)
    val = [-1] * (n + 1)
    level = 0
    while que:
        for _ in range(len(que)):
            node = que.popleft()
            val[node] = level
            for nei in adj[node]:
                ind[nei] -= 1
                if ind[nei] == 1:
                    que.append(nei)
            level += 1
    
    arr = []
    for node in range(1, n + 1):
        arr.append((degree[node], -val[node], node))
    arr.sort()

    ans = 1
    deg, _, first = arr.pop()
    ans += deg - 1
    for nei in adj[first]:
        degree[nei] -= 1
    arr = []
    for node in range(1, n + 1):
        if node != first:
            arr.append((degree[node], -val[node], node))
    arr.sort()
    deg, _, _ = arr.pop()
    ans += deg - 1
    print(ans)

    


    

tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()