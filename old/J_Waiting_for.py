import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    p = 0
    for _ in range(n):
        op = S().split()
        if op[0] == 'P':
            p += int(op[-1])
        else:
            b = int(op[-1])
            if b <= p:
                p -= b
                print("NO")
            else:
                p = 0
                print("YES")


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()