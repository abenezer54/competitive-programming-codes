import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    p = [0, 0] + IL()
    adj = [[] for _ in range(n + 1)]
    for node in range(2, n + 1):
        adj[p[node]].append(node)

    que = deque([1])
    ans = 0
    while que:
        ln = len(que)
        ans += ln % 2
        for _ in range(ln):
            node = que.popleft()
            for nei in adj[node]:
                que.append(nei)
    print(ans)


    

solve()
