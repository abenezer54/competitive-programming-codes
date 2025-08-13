import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = IL()
    ind = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]

    for i in range(n):
        ind[a[i]] += 1
        adj[i + 1].append(a[i])

    que = deque()
    for node in range(1, n + 1):
        if ind[node] == 0:
            que.append(node)
            
    level = 0
    while que:  
        for _ in range(len(que)):
            node = que.popleft()
            for nei in adj[node]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    que.append(nei)
        level += 1
    print(level + 2)




tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()