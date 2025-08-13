import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = IL()
    ans = deque()
    for val in a:
        if not ans or ans[0] >= val:
            ans.appendleft(val)
        else:
            ans.append(val)
    print(*ans)


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()