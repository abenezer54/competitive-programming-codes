import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = sorted(IL())
    # print(a)
    ans = []
    for i in range(n//2):
        ans.append(a[~i])
        ans.append(a[i])
    # print(n)
    if n % 2:
        ans.append(a[(n // 2)])
    ans.reverse()
    # d = []
    # for i in range(n - 1):
    #     d.append(abs(ans[i] - ans[i + 1]))
    # print(d)
    print(*ans)





tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()