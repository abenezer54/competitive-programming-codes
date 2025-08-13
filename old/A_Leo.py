import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    a, b, n = IL()
    cnt = 0
    while a <= n and b <= n:
        mn = min(a, b)
        mx = max(a, b)
        cnt += 1   
        b = mn + mx
        a = mx
    print(cnt) 


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()