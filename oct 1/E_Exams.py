import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = [IL() for _ in range(n)]
    a.sort()
    prev = 0
    for i in range(n):
        if a[i][1] >= prev:
            prev = max(prev, a[i][1])
        else:
            prev = a[i][0]
    print(prev)
solve()
