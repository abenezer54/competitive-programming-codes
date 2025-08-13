import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    d, r = n // m, n % m
    ans = []
    for i in range(m):
        val = d
        if r > 0:
            val += 1
        r -= 1
        ans.append(val)
    print(*sorted(ans))

solve()
