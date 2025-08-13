import os, sys
from collections import defaultdict
# sys.stdin = open("prescription.in", "r")
# sys.stdout = open("prescription.out", 'w')

input = lambda: sys.stdin.readline().strip()

n, m = list(map(int, input().split()))
a = []
for _ in range(m):
    a.append(list(map(int, input().split())))

cost = [0] +  list(map(int, input().split()))
ans = float('inf')
for mask in range(1 << m):
    cur = 0
    vis = [0] * (n + 1)
    for i in range(mask.bit_length()):
        if mask & (1 << i):
            for j in range(2, len(a[i])):
                vis[a[i][j]] += 11

                if a[i][0] == 1:
                    cur += cost[a[i][j]]
                else:
                    cur += cost[a[i][j]] / 2
        # print(mask, i)

    if vis.count(0) == 1:
        ans = min(ans, cur)
print('%.1f' % ans)

