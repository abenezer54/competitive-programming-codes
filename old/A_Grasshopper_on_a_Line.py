import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    x, k = IL()
    if x % k != 0:
        print(1)
        print(x)
        return
    else:
        for i in range(1, x):
            if i % k != 0 and (x - i) % k != 0:
                print(2)
                print(i, x - i)
                return


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()