import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = IL()
    tot = a.count(1)
    ans = -float('inf')
    for i in range(n):
        for j in range(i, n):
            cur = 0
            for k in range(i, j + 1):
                if a[k]:
                    cur -= 1
                else:
                    cur += 1
            cur += tot
            ans = max(ans, cur)
    print(ans)


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()