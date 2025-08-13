import os, sys

sys.stdin = open("committee.in", "r")
sys.stdout = open("committee.out", 'w')

input = lambda: sys.stdin.readline().strip()

n, m = list(map(int, input().split()))

vals = []
a = [list(map(int, input().split())) for _ in range(n)]
mn = float('inf')
mx = -float('inf')
for i in range(n):
    sm = 0
    for j in range(m):
        sm += a[i][j]
    mn = min(mn, sm)
    mx = max(mx, sm)
f1 = f2 = False
for i in range(n):
    sm  = 0
    for j in range(m):
        sm += a[i][j]
    if sm == mn and not f1:
        f1 = True
        ans1 = i + 1
    
    if sm == mx and not f2:
        f2 = True
        ans2 = i + 1
print(ans1, ans2)
