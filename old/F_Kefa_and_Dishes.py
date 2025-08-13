import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
from itertools import permutations
def solve():
    n, m, k = IL()
    a = IL()
    adj = defaultdict(int)
    if n == 1:
        print(a[0] + k)
        return
    for _ in range(k):
        x, y, c = IL()
        adj[(x, y)] = c
    mx = -float('inf')
    p = list(permutations(list(range(1, n + 1)), m))
    # print(p)
    for arr in p:
        cur = 0
        for i in range(len(arr) - 1):
            cur += a[arr[i] - 1]
            cur += adj[(arr[i], arr[i + 1])]
        cur += a[arr[-1] - 1]
        # print(arr, cur)
        mx = max(mx, cur)
    print(mx)



tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()