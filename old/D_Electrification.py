import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
# print(1000000000 - 500000000, 500000000 - 1 )
def solve():
    n, k = IL()
    a = sorted(IL())
    l = 0
    arr = []
    for r in range(n):

        if r - l + 1 == k + 1:
            mid = math.ceil((a[r] + a[l]) / 2)
            arr.append((max(abs(mid - a[l]), abs(mid - a[r])), mid))
            l += 1
    arr.sort()
    print(arr[0][1])


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()