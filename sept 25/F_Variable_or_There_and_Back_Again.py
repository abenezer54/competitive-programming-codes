import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    a = [0] + IL()
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = IL()
        adj[x].append(y)
    # print(a)
    vis = [0] * (n + 1)
    for node in range(1, n + 1):
        if a[node] == 1:
            # print(node)
            vis[node] = 2
            stack = [node]
            parent = [-1] * (n + 1)
            while stack:
                node = stack.pop()
                for nei in adj[node]:
                    if vis[nei] == 0:
                        if a[nei] == 0:
                            stack.append(nei)
                            parent[nei] = node
                            vis[nei] = 2
                        elif a[nei] == 2:
                            vis[nei] = 1
                            cur = node
                            while parent[cur] != -1:
                                vis[cur] = 1
                                cur = parent[cur]
                            vis[cur] = 1
    for node in range(1, n + 1):
        if vis[node] == 1:
            print(1)
        else:
            print(0)


    

solve()
