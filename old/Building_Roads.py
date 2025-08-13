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
    arr = []
    for start in range(1, n + 1):
        if not vis[start]:
            arr.append(start)
            vis[start] = True
            stack = [start]
            while stack:
                node = stack.pop()
                for nei in adj[node]:
                    if not vis[nei]:
                        vis[nei] = True
                        stack.append(nei)
    print(len(arr) - 1)
    for i in range(len(arr) - 1):
        print(arr[i], arr[i + 1], end='\n')


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()