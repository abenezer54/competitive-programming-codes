import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, t = IL()
    if t == 10:
        if n == 1:
            print(-1)
        else:
            print('1' + ('0' * (n - 1)))
    else:
        print(str(t) + ('0' * (n - 1)))
    


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()