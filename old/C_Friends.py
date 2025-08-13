import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    m = IL()[0]
    check = set()
    for _ in range(m):
        a, b = IL()
        check.add((a, b))
        check.add((b, a))
    for i in range(1, 6):
        for j in range(i + 1, 6):
            for k in range(j + 1, 6):
                if (i, j) in check and (i, k) in check and (j, k) in check:
                    print("WIN")
                    return
                if (i, j) not in check and (i, k) not  in check and (j, k) not in check:
                    print("WIN")
                    return
                 
    print("FAIL")
    



tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()