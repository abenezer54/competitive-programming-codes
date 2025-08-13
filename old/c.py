import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    x = IL()[0]

    l, r = 0, int(1e18)
    while l + 1 < r:
        mid = (l + r) // 2
        if ((mid + 1) * mid) // 2 >= x:
            r = mid
        else:
            l = mid
    val =  (r * (r + 1)) // 2
    diff  = val - x
    if diff == 1:
        r += 1
    print(r)
       
tt = IL()[0]
for _ in range(tt):
    solve()