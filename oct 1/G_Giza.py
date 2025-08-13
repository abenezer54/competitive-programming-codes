import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = [0] + IL()
    adj = defaultdict(list)
    for _ in range(n - 1):
        i, j = IL()
        adj[i].append(j)
        adj[j].append(i)
    vis = [0] * (n + 1)
    ans = 0
    for i in range(1, n + 1):
        if vis[i] == 0:
            # print(n, i)
            stack = [i]
            vis[i] = 1
            while stack:
                node = stack.pop()
                for nei in adj[node]:
                    if vis[nei] == 0 and a[nei] == a[node]:
                        stack.append(nei)
                        vis[nei] = 1
            ans += 1
    print(ans)
    

for _ in range(II()):
    solve()
