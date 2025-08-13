import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    a = IL()
    cur = 1
    mx = 1

    for i in range(1, n):
        if a[i] == a[i - 1]:
            cur = 1
        else:
            cur += 1
        mx = max(mx, cur)
    print(mx)




tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()