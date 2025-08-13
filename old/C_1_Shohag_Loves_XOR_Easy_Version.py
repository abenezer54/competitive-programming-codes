import sys, math, random; from heapq import heapify, heappop, heappush
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    x, m = IL()
    ans = 0
    for y in range(1, min((x << 1) + 1, m + 1)):
        val = y ^ x
        if y != x and val != 0 and (y % val == 0 or x % val == 0):
            ans += 1
    print(ans)

tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()