import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, budget = IL()
    a = IL()
    cost = []
    for i in range(n):
        cost.append(a[i] + (i + 1))
    if min(cost) > budget:
        print(0, 0)
        return

    def check(mid):
        cost = []
        for i in range(n):
            cost.append(a[i] + ((i + 1) * mid))
        cost.sort()

        tot = 0
        for i in range(mid):
            tot += cost[i]
        return tot <= budget
    
    def find(mid):
        cost = []
        for i in range(n):
            cost.append(a[i] + ((i + 1) * mid))
        cost.sort()

        tot = 0
        for i in range(mid):
            tot += cost[i]
        return tot 
    

    l, r = 1, n + 1
    while l + 1 < r:
        mid = (l + r) // 2
        if check(mid):
            l = mid
        else:
            r = mid
    K = l
    print(K, find(K))


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()