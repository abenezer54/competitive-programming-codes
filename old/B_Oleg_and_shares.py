import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    a = IL()
    mn = min(a)
    ans = 0
    for i in range(n):
        if (a[i] - mn) % k != 0:
            print(-1)
            return
        else:
            ans += (a[i] - mn) // k
    print(ans)


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()