import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m, k = IL()
    a = IL()
    q = IL()
    exist = [0] * (n + 1)
    for val in q:
        exist[val] = 1
        
    if exist.count(1) == n:
        print('1' * m)
        return
    if exist.count(1) < n - 1:
        print('0' * m)
        return
    
    ans = [0] * m
    for i in range(m):
        if not exist[a[i]]:
            ans[i] = 1
    print(''.join(map(str, ans)))

tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()