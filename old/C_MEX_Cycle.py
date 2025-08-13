import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, x, y = IL()
    ans = [0] * (n)
    diff = y - x
    if n & 1:
        for i in range(1, n - 1, 2):
            ans[i] = 1
        ans[-1] = 2
    else:
        for i in range(1, n, 2):
            ans[i] = 1

    if diff == 1 or (x == 1 and y == n):
        print(*ans)
        return
    
    if n % 2 == 0 and diff % 2 == 0:
        ans[x - 1] = 2

    if n & 1 and diff % 2 == 1 and y != n:
        ans = [0] * (n)
        cnt = 0
        for i in range(x - 1, -1, -1):
            if cnt & 1:
                ans[i] = 1
            cnt += 1
        
        i = n - 1
        while cnt != n:
            if cnt & 1:
                ans[i] = 1
    
            i -= 1
            cnt += 1
        i -= 1
        ans[i] = 2
    print(*ans)


    
tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()