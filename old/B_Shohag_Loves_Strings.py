import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    s = S()
    n = len(s)
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            print(s[i:i + 2])
            return
        if i < n - 1 and i + 2 < n:
            cur = set([s[i], s[i + 1], s[i + 2]])
            if len(cur) == 3:
                print(s[i: i + 3])
                return
    print(-1)
    



tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()