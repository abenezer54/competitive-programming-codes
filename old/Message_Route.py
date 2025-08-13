import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = IL()
        adj[a].append(b)
        adj[b].append(a)

    vis = [False] * (n + 1)
    vis[1] = True
    que = deque([1])
    parent = [-1] * (n + 1)
    def find_path(node):
        path = [node]
        while parent[node] != -1:
            path.append(parent[node])
            node = parent[node]
        return path[::-1]
    
    while que:
        node = que.popleft()
        if node == n:
            path = find_path(node)
            print(len(path))
            print(*path)
            return 
        
        for nei in adj[node]:
            if not vis[nei]:
                vis[nei] = True
                que.append(nei)
                parent[nei] = node
         

    print("IMPOSSIBLE")
tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()