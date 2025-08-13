import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    ind = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = IL()
        ind[u] += 1
        ind[v] += 1
        adj[u].append(v)
        adj[v].append(u)
    
    arr = [(ind[i], i) for i in range(1, n + 1)]
    arr.sort()
    components = 1
    val, first = arr.pop()
    components += val - 1
    


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()