import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, d, k = IL()
    p = [0] * (n + 2)
    for _ in range(k):
        l, r = IL()
        left = max(1, l - d + 1)
        p[left] += 1
        p[r + 1] -= 1
    for i in range(1, n + 2):
        p[i] += p[i - 1]
    p = p[1:-d]
    mx, mn = max(p), min(p)
    # print(p)
    print(p.index(mx) + 1, p.index(mn) + 1)
    

for _ in range(II()):
    solve()
