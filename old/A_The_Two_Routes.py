import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        x, y = IL()
        adj[x].add(y)
        adj[y].add(x)
    
    def bfs(type):
        que = deque([1])
        vis = [0] * (n + 1)
        vis[1] = 1
        level = 0
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if node == n:
                    return level
                if type == 1:
                    for nei in adj[node]:
                        if vis[nei] == 0:
                            que.append(nei)
                            vis[nei] = 1
                else:
                    for nei in range(1, n + 1):
                        if nei not in adj[node] and nei != node:
                            if vis[nei] == 0:
                                que.append(nei)
                                vis[nei] = 1
            level += 1
        return -1
    
    one, two = bfs(1), bfs(2)
    if min(one, two) == -1:
        print(-1)
        return
    print(max(one, two))


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()