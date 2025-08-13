import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    s = S()
    cnt = Counter(s)
# pri'nt(cnt)
    a, b = 0, 0
    for  v in cnt.values():
        if v > 1:
            a += 1
        else:
            b+= 1
    print(a + (b // 2))


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()