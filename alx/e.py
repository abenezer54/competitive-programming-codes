import os, sys
from collections import defaultdict
sys.stdin = open("connected.in", "r")
sys.stdout = open("connected.out", 'w')

input = lambda: sys.stdin.readline().strip()

n, m = list(map(int, input().split()))
adj = defaultdict(list)
for _ in range(m):
    a, b = list(map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)

vis = [0] * (n + 1)
prev = -1
ans = []
ind = [0] * (n + 1)
for start in range(1, n + 1):
    if vis[start] == 0:
        if prev != -1:
            ans.append((start, prev))
            ind[prev] += 1
            ind[start] += 1
        prev = start

        stack = [start]
        while stack:
            node = stack.pop()

            for nei in adj[node]:
                if vis[nei] == 0:
                    stack.append(nei)
                    vis[nei] = 1
print(max(ind))
print(len(ans))
for val in ans:
    print(*val)


