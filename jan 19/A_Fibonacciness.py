import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    a = IL()
    ans = 0
    for x in range(-1000, 1000):
        cur = 0
        if a[0] + a[1] == x:
            cur += 1
        if a[1] + x == a[2]:
            cur += 1
        if x + a[2] == a[3]:
            cur += 1
        ans = max(ans, cur)
    print(ans)


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()