import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = IL()
        adj[u].append(v)
        adj[v].append(u)
    arr = set()

    for start in range(1, n + 1):
        move = 0
        que = deque([start])
        vis = [0] * (n + 1)
        vis[start] = 1
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if (move & 1 and move > 1):
                    arr.add((min(node, start), max(node, start)))
                
                for nei in adj[node]:
                    if vis[nei] == 0:
                        que.append(nei)
                        vis[nei] = 1
            move += 1


    step = 1
    if len(arr) & 1:
        print("First", flush=True)
    else:
        print("Second", flush=True)
        step = 0

    while True:
        if step & 1:
            i, j = arr.pop()
            print(i, j, flush=True)
        else:
            i, j = IL()
            if i == -1 and j == -1:
                return
            arr.discard((i, j))

        step += 1



tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()