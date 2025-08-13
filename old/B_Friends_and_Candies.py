import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = IL()
    sm = sum(a)
    if sm % n != 0:
        print(-1)
        return
    ans = 0
    for num in a:
        if num > sm // n:
            ans += 1
    print(ans)


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()