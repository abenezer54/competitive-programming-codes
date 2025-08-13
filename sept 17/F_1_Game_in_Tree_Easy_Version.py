import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x, y = IL()
        adj[x].append(y)
        adj[y].append(x)

    u, v = IL()



    stack = [(1, 0)]
    vis = [0] * (n + 1)
    vis[1] = 1

    alice = [0] * (n + 1)
    while stack:
        node, w = stack.pop()
        alice[node] = w
    
        for nei in adj[node]:
            if vis[nei] == 0:
                stack.append((nei, w + 1))
                vis[nei] = 1
                
    alice[u] = 0
    # print(alice)
    stack = [(u, 0)]
    vis = [0] * (n + 1)
    vis[u] = 1
    bob = 0
    while stack:
        node, w = stack.pop()
        bob = max(bob, w)

        for nei in adj[node]:
            if vis[nei] != 1:
                if w + 1 < alice[nei]:
                    alice[nei] = 0
                    stack.append((nei, w + 1))

    mx = max(alice)
    # print(mx, level - 1)
    if mx >= bob:
        print("Alice")
    else:
        print("Bob")


for _ in range(II()):
    solve()
