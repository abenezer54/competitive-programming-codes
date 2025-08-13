import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = []
    for i in range(1, n + 1):
        a.append(pow(2, i))
    cur = a[-1]
    for i in range((n//2) - 1):
        cur += a[i]
    # print(cur)
    print(abs(cur - (sum(a) - cur)))

for _ in range(II()):
    solve()
