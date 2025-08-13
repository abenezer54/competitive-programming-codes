import os, sys
from collections import defaultdict
sys.stdin = open("tourney.in", "r")
sys.stdout = open("tourney.out", 'w')

input = lambda: sys.stdin.readline().strip()

n, m = list(map(int, input().split()))

alter = [0] * (n + 1)
last = ['N'] * (n + 1)

for _ in range(m):
    cmd, city = input().split()
    city = int(city)
    if last[city] != cmd:
        alter[city] += 1
    last[city] = cmd
# print(last)

ans = []
mx = max(alter)
changes = []
count = 0
for city in range(1, n + 1):
    if last[city] == 'D':
        ans.append(city)
    if alter[city] == mx:
        changes.append(city)
    
    if alter[city] == 0:
        count += 1
print(*ans)
print(*changes)
print(count)
