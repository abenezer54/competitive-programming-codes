import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    ind = [0] * (n + 1)
    adj = defaultdict(list)
    for _ in range(n - 1):
        a, b = IL()
        adj[a].append(b)
        adj[b].append(a)
        ind[a] += 1
        ind[b] += 1
    arr = []
    mp = defaultdict(int)
    for node in range(1, n + 1):
        for nei in adj[node]:
        
            if ind[nei] == 2:
                # if node == 2:
                #     print(nei)
                mp[node] += 1
    print(mp)
    for node in range(n + 1):
        if ind[node] == 2:
            arr.append(node)
    print(arr, mp[2])
    ans = 0
    for node in arr:
        if node == 4:
            print('here', mp[4])
        tot = len(arr) - 1 - mp[node]
        ans += max(0, tot)
    print(ans)

tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()