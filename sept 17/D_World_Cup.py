import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = IL()
    val = []
    for i in range(n):
        a[i] = max(0, a[i] - i)
        val.append(math.ceil(a[i]/n))
    print(val.index(min(val)) + 1)

solve()
