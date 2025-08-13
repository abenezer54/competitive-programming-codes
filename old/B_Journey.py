import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, a, b, c = IL()
    tot = a + b + c
    x = n // tot
    ans = 3 * x
    n -= tot * x
    if n > 0:
        if n <= a:
            ans += 1
        elif n <= a + b:
            ans += 2
        else:
            ans += 3
    print(ans)
    


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()