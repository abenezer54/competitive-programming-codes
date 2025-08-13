import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = IL()
        adj[a].append(b)
        adj[b].append(a)

    col = [0] * (n + 1)
    for start in range(1, n + 1):
        if col[start] == 0:
            stack = [start]
            col[start] = 1
            while stack:
                node = stack.pop()
                for nei in adj[node]:
                    if col[nei] == 0:
                        if col[node] == 1:
                            col[nei] = 2
                        else:
                            col[nei] = 1
                        stack.append(nei)
                    else:
                        if col[nei] == col[node]:
                            print("IMPOSSIBLE")
                            return
    print(*col[1:])



tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()