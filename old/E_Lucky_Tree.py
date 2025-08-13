import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def is_lucky(num):
    for char in str(num):
        if not (char == '4' or char == '7'):
            return False
    return True


def solve():
    n = IL()[0]
    adj = [defaultdict(int) for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v, w = IL()
        adj[v][u] = w
        adj[u][v] = w
    
    parent = [-1] * (n + 1)
    tot = [0] * (n + 1)
    from_childs = [defaultdict(int) for _ in range(n + 1)]

    stack = [1]
    # print(adj)
    vis = [0] * (n + 1)
    vis[1] = 1
    while stack:
        # print('stack', stack)
        node = stack[-1]

        for nei in adj[node]:
            if vis[nei] == 0:
                stack.append(nei)
                parent[nei] = node
                vis[nei] = 1
        
        if node == stack[-1]:

            stack.pop()
            if parent[node] != -1:
                val = tot[node]
                if is_lucky(adj[node][parent[node]]) or val:
                    val += 1

                from_childs[parent[node]][node] = val
                tot[parent[node]] += val
    ans = 0
    for node in range(1, n + 1):
        if parent[node] != -1:
            if node == 2:
                print('here', tot[node])
            tot[node] += tot[parent[node]] - from_childs[parent[node]][node]
            if is_lucky(adj[parent[node]][node]):
                tot[node] += 1
            # if node == 2:
            #     print('here2', tot[node])
        ans += math.perm(tot[node], 2)
    print(tot)
    print(from_childs[1], parent[2])
    print(ans)
    

tt = 1
for _ in range(tt):
    solve()