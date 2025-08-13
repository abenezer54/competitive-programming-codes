import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = IL()
    check = sorted(list(range(1, (n * 2)+ 1)))
    c = a.copy()
    mn = float('inf')
    cnt = 0
    for i in range(1200):
        if a == check:
            mn = min(mn, cnt)
            break
        if i & 1:
            for j in range(0, (2 * n), 2):
                a[j], a[j + 1] = a[j + 1], a[j]
        else:
            for j in range(0, n):
                a[j], a[j + n] =  a[j + n], a[j]
        cnt += 1

    a = c.copy()
    # print(a)
    cnt = 0
    for i in range(1200):
        if a == check:
            mn = min(mn, cnt)
            break
        if not(i & 1):
            for j in range(0, (2 * n), 2):
                a[j], a[j + 1] = a[j + 1], a[j]
        else:
            for j in range(0, n):
                a[j], a[j + n] =  a[j + n], a[j]
    
        cnt += 1    

    if mn == float('inf'):
        print(-1)
    else:
        print(mn)


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()