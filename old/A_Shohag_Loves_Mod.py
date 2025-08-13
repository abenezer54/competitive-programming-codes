import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = [2, 3]
    val = 2
    for i in range(n - 2):
        i += 3
        a.append(i + val)
        val += 1
    print(*a)
    # for i in range(n):
    #     print(a[i] % (i + 1))
    




tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()