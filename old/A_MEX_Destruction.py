import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = IL()
    ans = 0
    for i in range(n):
        if a[i]:
            if i == 0:
                ans += 1
            else:
                if a[i - 1] == 0:
                    ans += 1
    print(min(ans, 2))



tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()