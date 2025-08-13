import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    def check(num):
        s = str(num)
        tot = 0
        for i in range(len(s)):
            for j in range(i):
                d = i - j
                p = pow(10, d - 1)
                val = int(s[j]) * p
                tot += val
            if int(s[i]) >= 4:
                tot += 1
        return tot 
    k = IL()[0]

    l = k - 1
    r = int(1e18)
    # print(check(25))
    while l + 1 < r:
        mid = (l + r) // 2
        # print('mid: ', mid , check(mid))
        # print(check(mid) >= mid - k)
        if mid - check(mid) >= k:
            r = mid
        else:
            l = mid
    print(r, check(r))



tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()