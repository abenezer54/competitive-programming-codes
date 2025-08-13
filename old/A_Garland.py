import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    # n = IL()[0]
    s = S()
    cnt = Counter(s)
    if len(cnt) == 1:
        print(-1)
    elif len(cnt) == 4:
        print(4)
    elif len(cnt) == 2 and 1 in cnt.values():
        print(6)
    else:
        print(4)



tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()