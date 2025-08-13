import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
# print(-1 % 3)
def convert(num):
    val = []
    while num > 0:
        val.append(num % 3)
        num //= 3
    val.reverse()
    return val
def solve():
    a, c = IL()
    x, y = convert(a), convert(c)
    if len(x) < len(y):
        diff = len(y) - len(x)
        x = ([0] * (diff)) + x
    elif len(x) > len(y):
        diff = len(x) - len(y)
        y = ([0] * diff) + y
    x.reverse()
    y.reverse()
    # print(x, y)
    ans = 0
    for i in range(len(x)):
        diff = x[i] - y[i]
        if diff < 0:
            ans += (-diff) * pow(3, i)
        elif diff > 0:
            ans += (3 - diff) * pow(3, i)
            

    print(ans)

tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()