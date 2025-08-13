import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = IL()
    cnt = [0] * 32

    for i in range(n):
        for j in range(32):
            if a[i] & (1 << j):
                cnt[j] += 1
    # print(cnt)
    ans = []
    for num in range(1, n + 1):
        ok = True
        for val in cnt:
            if val % num != 0:
                ok = False
        if ok:
            ans.append(num)
    print(*ans)


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()