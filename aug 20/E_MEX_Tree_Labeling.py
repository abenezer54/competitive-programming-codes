import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    ind  = [0] * (n + 1)
    adj = defaultdict(list)
    mp = defaultdict(int)
    for idx in range(n - 1):
        u, v = IL()
        ind[v] += 1
        ind[u] += 1
        adj[v].append(u)
        adj[u].append(v)
        mp[(u, v)] = idx
        mp[(v, u)] = idx

    que = deque()
    for v in range(1, n + 1):
        if ind[v] == 1:
            que.append(v)
    # print(adj)
    # print(que)
    ans = [-1] * (n - 1)
    cur = 0
    vis = set()
    while que:
        node = que.popleft()
        # print('node', node)
        for nei in adj[node]:
            if not (nei, node) in vis:
                idx = mp[(node, nei)]
                if ans[idx] == -1:
                    ans[idx] = cur
                    cur += 1
                vis.add((nei, node))
                vis.add((node, nei))
            ind[nei] -= 1
            if ind[nei] == 1:
                que.append(nei)
    
        
    for val in ans:
        print(val)

solve()


