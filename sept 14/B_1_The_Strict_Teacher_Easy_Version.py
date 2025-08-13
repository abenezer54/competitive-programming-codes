import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m, q = IL()
    arr = IL()
    a, b  = min(arr), max(arr)
    start = II()
    if start == a or start == b:
        print(0)
        return
    if start > a and start < b:
        mid = (a + b) // 2
        print(min(abs(a - mid), abs(b - mid)))
    elif start < a:
        print(a - 1)
    else:
        print(n - b)

for _ in range(II()):
    solve()
