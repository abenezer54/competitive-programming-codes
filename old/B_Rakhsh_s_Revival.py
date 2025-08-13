import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m, k = IL()
    s = S()
    cur = 0
    last = -float('inf')
    ans = 0
    for i in range(n):
        ln = i - last + 1
        if s[i] == '0' and ln > k:
            cur += 1
        else:
            cur = 0

        if cur == m:
            last = i
            ans += 1
            cur = 0

    print(ans)

tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()