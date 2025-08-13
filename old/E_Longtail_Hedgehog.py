import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = IL()
        adj[u].append(v)
        adj[v].append(u)
    best = defaultdict(list)
    xx = defaultdict(int)

    vis = [0] * (n + 1)
    ans = 0
    parent = [-1] * (n + 1)
    for start in range(1, n + 1):
        if vis[start] == 0:
            stack = [(start, 1)]
            vis[start] = 1
            while stack:
                node, length = stack[-1]
                # print(node)
                vis[node] = length
                ans = max(ans, length * len(adj[node]))
                for nei in adj[node]:
                    if nei > node:
                        if vis[nei] == 0:
                            # print('node, nei', node, nei)
                            stack.append((nei, length + 1))
                            parent[nei] = node
                            xx[nei] = length
                            vis[nei] = 1
                        else:
                            print('here', node, nei)
                            if nei in best:
                                diff = length - xx[nei]
                                print("get", diff, best[nei])
                                ans = max(ans, best[nei][1] * (best[nei][0] + diff ))
                if node == stack[-1][0]:
                    stack.pop()
                    par = parent[node]
                    if par != -1:
                        if not best[par]:
                            best[par] = [length, len(adj[node])]
                        else:
                            prev = best[par][0] * best[par][1]
                            now = length *  len(adj[node])
                            if now > prev:
                                best[par] = [length, len(adj[node])]
                    else:
                        best[node] = [length, len(adj[node])]
                        

    print(ans)
tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()