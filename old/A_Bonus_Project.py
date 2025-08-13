import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    a = IL()
    b = IL()
    ans = []
    for i in range(n):
        ans.append(a[i]//b[i])
    tot = sum(ans)
    diff = tot - k
    if diff < 0:
        print(*([0] * n))
        return 
    
    for i in range(n):
        if diff > 0:
            mn = min(diff, ans[i])
            ans[i] -= mn
            diff -= mn
    print(*ans)


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()