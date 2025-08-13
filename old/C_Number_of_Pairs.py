import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, L, R = IL()
    a = sorted(IL()) 
    # print(a)
    ans = 0
    for i in range(n):
        x = max(i + 1, bisect_left(a, L - a[i]))
        y = max(i + 1, bisect_right(a, R - a[i]))
        # if i == 0:
        #     print(x, y)
        # if x > i:
        if y > x:
            ans += max(0, y - x)
    print(ans)



tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()