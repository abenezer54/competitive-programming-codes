import sys
from math import ceil, gcd, log2
import heapq
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    # print(n)
    ind = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = IL()
        ind[u] += 1
        ind[v] += 1
        adj[v].append(u)
        adj[u].append(v)

    child = defaultdict(int)
    que = deque()
    for v in range(2, n + 1):
        if ind[v] == 1:
            que.append(v)
            child[v] = 0
            
        
    par = defaultdict(int)
    nxt = defaultdict(list)
    next_best = defaultdict(int)
    while que:
        node = que.popleft()
        # print(node, nxt[node])
        if len(nxt[node]) == 2:
            val1 = child[nxt[node][1]] + next_best[nxt[node][0]]
            val2 = child[nxt[node][0]]  + next_best[nxt[node][1]]
            next_best[node] = max(val1, val2)

        for nei in adj[node]:
            if par[nei] != node:
                child[nei] += child[node] + 1
                next_best[nei] = max(next_best[nei], child[node])
                par[node] = nei
                nxt[nei].append(node)
            ind[nei] -= 1
            if ind[nei] == 1 :
                que.append(nei)
    print(nxt)
    if len(nxt[1]) == 1:
        print(child[nxt[1][0]])
        return
    else:
        val1 = child[nxt[1][1]] + next_best[nxt[1][0]]
        val2 = child[nxt[1][0]]  + next_best[nxt[1][1]]
        print(max(val1, val2))
    # print(next_best)
    # print(ans)

    



for _ in range(II()):
    solve()
