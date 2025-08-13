import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = b = c = n
    def check(mid):
        if mid % 2 == 0:
            val = mid + (mid // 2)
            return val, val
        else:
            val = (mid - 1) + (mid // 2)
            return val + 1, val + 2
        
    
    l, r = 0, 2000
    while l + 1 < r:
        mid = (l + r) // 2
        x, y = check(mid)
        if x >= n and y >= n:
            r = mid
        else:
            l = mid
    ans = r
    x, y = check(r)
    d = [x - n, y - n]
    if d.count(1) == 2 and n & 1:
        ans -= 1
    ans += (n + 1) // 2 

    print(ans)
tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()