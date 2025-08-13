import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def cv(a): return ord(a) - 97
def solve():
    first = S()
    second = S()
    if len(first) != len(second):
        print(-1)
        return

    n = IL()[0]
    adj = [[float('inf')] * 26 for _ in range(26)]
    for _ in range(n):
        x, y, w = input().split()
        w = int(w)
        # print(adj)
        adj[cv(x)][cv(y)] = min(adj[cv(x)][cv(y)], w)
        
    shortest = []
    for start in range(26):
        sh = [-1] * 26
        heap = [(0, start)]
        vis = [0] * 26
        while heap:
            w, node = heappop(heap)
            if vis[node] == 1:
                continue
            vis[node] = 1
            sh[node] = w
            for j in range(26):
                if vis[j] == 0 and adj[node][j] != float('inf'):
                    heappush(heap, (adj[node][j] + w, j))
        shortest.append(sh)

    for i in range(26):
        shortest[i][i] = 0

    tot = 0
    ans = []
    for i in range(len(first)):
        mn = float('inf')
        cur = -1
        for j in range(26):
            x = shortest[cv(first[i])][j] 
            y = shortest[cv(second[i])][j] 
            if -1 not in (x, y):
                if x + y < mn:
                    mn = x + y
                    cur = chr(j + 97)
        if mn == float('inf'):
            print(-1)
            return
        tot += mn
        ans.append(cur)

    print(tot)
    print(''.join(ans))

    


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()