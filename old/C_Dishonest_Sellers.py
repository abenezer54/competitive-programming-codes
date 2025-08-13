import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    a = IL()
    b = IL()
    arr = [(a[i], b[i]) for i in range(n)]
    arr.sort(key=lambda x: x[0] - x[1])
    ans = 0
    # print(arr)
    for i in range(n):
        if i < k:
            ans += arr[i][0]
        else:
            ans += min(arr[i])
    print(ans)



tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()