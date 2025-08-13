import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    mn = math.ceil(n / 2)
    mx = n
    for x in range(mn, mx + 1):
        if x >= m and x % m == 0:
            print(x)
            return
    print(-1)

tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()