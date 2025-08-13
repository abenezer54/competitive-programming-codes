import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = [0] + IL()
    # print(a)
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = IL()
        adj[u].append(v)
        adj[v].append(u)

    ans = -float('inf')
    sums = [[] for _ in range(n + 1)]
    best = [[] for _ in range(n + 1)]
    stack = [1]
    parent = [-1] * (n + 1)
    vis = [0] * (n + 1)
    vis[1] = 1
    while stack:
        node = stack[-1]
        for nei in adj[node]:
            if vis[nei] == 0:
                stack.append(nei)
                parent[nei] = node
                vis[nei] = 1

        if node == stack[-1]:
            stack.pop()
            if parent[node] != -1:
                par = parent[node]
                tot = sum(sums[node]) + a[node]
                sums[par].append(tot)
                cur_best = max(best[node]) if best[node] else - float('inf')
                best[par].append(max(cur_best, tot))
            if len(best[node]) >= 2:
                arr = sorted(best[node])
                ans = max(ans, arr[-1] + arr[-2])
        


            
    if ans == -float('inf'):
        print("Impossible")
    else:
        print(ans)




tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()