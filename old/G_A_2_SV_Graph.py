import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    c = S()
    if c == "A":
        print(5, 5)
        print(5, 2)
        print(3, 1)
        print(4, 2)
        print(1, 4)
        print(1, 2)
    if c == '2':
        # print(4, 3)
        # print(1, 2)
        # print(2, 3)
        # print(3, 4)
        



        print(6, 5)
        print(1, 2)
        print(2, 3)
        print(3, 4)
        print(4, 5)
        print(5, 6)
    if c == 'S':
        # print(4, 3)
        # print(1, 2)
        # print(2, 3)
        # print(3, 4)

        print(6, 5)
        print(1, 2)
        print(2, 3)
        print(3, 4)
        print(4, 5)
        print(5, 6)
    if c == 'V':
        print(3, 2)
        print(1, 2)
        print(1, 3)


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()