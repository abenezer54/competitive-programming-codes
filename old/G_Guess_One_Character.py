import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def query(val):
    print(1, val, flush=True)
    res = IL()[0]
    return res

def ans(pos, val):
    print(0, pos, val, flush=True)
    IL()

def solve():
    n = IL()[0]

    res = query('1')
    zeros = n - res
    if res == 0:
        ans(1, '0')
        return
    if res == n:
        ans(1, '1')
        return
    
    res = query('01')
    zeros -= res
    if res == 0:
        ans(1, '1')
        return
    res = query('00')
    zeros -= res
    if zeros > 0:
        ans(n, 0)
    else:
        ans(n, 1)

    


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()