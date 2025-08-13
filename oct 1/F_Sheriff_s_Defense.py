import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, c = IL()
    a = [0] + IL()
    adj = defaultdict(list)
    for _ in range(n - 1):
        u, v = IL()
        adj[u].append(v)
        adj[v].append(u)

    dp = defaultdict(tuple)
    stack = [1]
    vis = [0] * (n + 1)
    vis[1] = 1
    parent = [-1] * (n + 1)
    while stack:
        node = stack[-1]
        if len(adj[node]) == 1 and node != 1:
            dp[node] =(0, a[node])

        for nei in adj[node]:
            if vis[nei] == 0:
                parent[nei] = node
                stack.append(nei)
                vis[nei] = 1

        if node == stack[-1]:
            stack.pop()
            par = parent[node]

            take = 0
            leave = 0
            for nei in adj[node]:
                if nei != par :
                    # print('inside', node, nei)
                    leave += max(dp[nei])
                    take += max(dp[nei][0], dp[nei][1] - (2 * c))
            if node not in dp:
                dp[node] = (leave, take + a[node])
    print(max(dp[1]))

            


    

for _ in range(II()):
    solve()
