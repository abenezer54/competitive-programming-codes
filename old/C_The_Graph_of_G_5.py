import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    a, b = IL()
    ait = [1, 2, 3, 4]
    aa = [5, 6, 7]
    astu = [8, 9]
    if a in ait and b in ait:
        print("Yes")
    elif a in aa and b in aa:
        print("Yes")
    elif a in astu and b in astu:
        print("Yes")
    else:
        print("No") 


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()