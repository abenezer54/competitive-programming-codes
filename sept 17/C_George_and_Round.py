import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    a = IL()
    b = IL()
    i = j = 0
    while i < n and j < m:
        # print(i, j)
        if a[i] <= b[j]:
            i += 1
            j += 1
        else:
            j += 1
    # print(i)
    print(n - i)
    

solve()
