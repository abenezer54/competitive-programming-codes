import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    a = IL()
    cnt = a.count(0)
    if cnt <= k:
        print(n)
        print(*([1] * n))
        return

    
    x, y = 0, -1
    zero = 0
    l = 0
    for r in range(n):
        if a[r] == 0:
            zero += 1
        
        while zero > k:
            if a[l] == 0:
                zero -= 1
            l += 1
        if (y - x + 1) < (r - l + 1):
            x = l
            y = r
    for i in range(n):
        if x <= i <= y:
            a[i] = 1

    print(y - x + 1)
    print(*a)




tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()