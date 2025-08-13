import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    adj = [[] for _ in range(n + 1)]
    ind = [0] * (n + 1)

    for _ in range(m):
        a, b = IL()
        adj[a].append(b)
        adj[b].append(a)
        ind[a] += 1
        ind[b] += 1
    
    shortest = defaultdict()
    que = deque([])
    for node in range(1, n + 1):
        if ind[node] == 1:
            que.append(node)
            shortest[node] = 0
            ind[node] -= 1
    # print(que, ind)
    vals = defaultdict(list)
    mx = defaultdict(int)
    while que:

        node = que.popleft()
        # print(node)
        vals[node].sort()
        ln = len(vals[node])
        if ln == 0:
            shortest[node] = 0
            mx[node] = 0
        elif ln == 1:
            shortest[node] = vals[node][0]
            mx[node] = vals[node][0]
        else:
            shortest[node] = vals[node][-1] + vals[node][-2] 
            mx[node] = max(vals[node][-1], vals[node][-2])

        for nei in adj[node]:
            # print(nei)
            ind[nei] -= 1
            vals[nei].append(mx[node] + 1)
            if ind[nei] == 1:
                que.append(nei)
    # print(shortest)
    ans = 0
    for v in shortest.values():
        ans = max(ans, v)
    print(ans)


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()