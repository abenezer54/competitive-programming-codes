import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    adj = [set() for _ in range(n + 2)]
    aa = [0] * (n + 3)
    bb = [0] * (n + 2)
    for node in range(2, n + 1):
        p, a, b = IL()
        adj[p].add(node)
        aa[node] = a
        bb[node] = b

    ans = [0] * (n + 1)
    stack = [1]
    A = aa[1]
    prefix = [bb[1]]
    vis = [0] * (n + 1)
    vis[1] = 1

    while stack:
        node = stack[-1]

        for nei in adj[node]:
            if vis[nei] == 0:
                vis[nei] = 1
                A += aa[nei]
                prefix.append(prefix[-1] + bb[nei])
                stack.append(nei)
                adj[node].remove(nei)
                break
        if node == stack[-1]:
            stack.pop()
            val = bisect_right(prefix, A) - 1
           
            ans[node] = val
            A -= aa[node]
            prefix.pop()
    print(*ans[2:])
    
        



tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()