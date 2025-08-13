import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = IL()
    if 0 not in a:
        print(0)
        return
    
    cnt = Counter(a)
    arr = sorted([val for val in cnt.keys()])
    i = 0
    while i < len(arr) and i == arr[i]:
        i += 1
    last = i
    dp1 = []
    for i in range(last):
        dp1.append((cnt[i] - 1) * last)
    # print(cnt)
    # print(dp1)
    for op in range(last - 2):
        dp2 = [float('inf')] * last
        # dp2[-1] = 0
        
        for i in range(last - 2, -1, -1):
           dp2[i] = dp1[i] + ((cnt[i] - 1) * i) + 1
        # print(dp2)
        dp1 = dp2
    print(min(dp2))
    # print(min(dp/[last - 1]))
# 



tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()