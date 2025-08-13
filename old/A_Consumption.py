import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = IL()
    b = IL()
    b.sort(reverse=True)
    tot = sum(a)
    mx = b[0] + b[1]
    if mx >= tot:
        print("YES")
    else:
        print("NO")


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()