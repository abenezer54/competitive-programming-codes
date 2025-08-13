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
    par = [-1] * (n + 1)
    ans = 0
    for start in range(1, n + 1):
        if col[start] == 0:
            col[start] = 1
            found = False
            stack = [start]
            while stack:
                node = stack.pop()
                for nei in adj[node]:
                    if col[nei] == 0:
                        stack.append(nei)
                        col[nei] = 1
                        par[nei] = node
                    else:
                        if nei != par[node]:
                            found = True
            if not found:
                ans += 1
    print(ans)


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()