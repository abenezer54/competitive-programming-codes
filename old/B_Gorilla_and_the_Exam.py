import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    a = IL()
    rand = 1
    x = Counter()
    for val in a:
        x[val ^ rand] += 1

    cnt = [val for val in x.values()]
    cnt.sort()

    j = 0
    ans = len(cnt)
    while j < (len(cnt) - 1) and cnt[j] <= k:
        ans -= 1
        k -= cnt[j]
        j += 1
    print(ans)


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()