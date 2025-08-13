import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    s = S()
    t = S()
    cnt = 0
    x = set()
    y = set()
    for i in range(n):
        if s[i] != t[i]:
            x.add(s[i])
            y.add(t[i])
            cnt += 1
    if cnt == 0:
        print("Yes")
        return
    if cnt == 2 and len(x) == 1 and len(y) == 1:
        print("Yes")
    else:
        print("No")


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()