import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    m = IL()[0]
    if m == 7 or m == 2:
        print("Yes")
    else:
        print("No")


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()