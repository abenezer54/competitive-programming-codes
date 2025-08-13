import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    arr = set()
    for _ in range(m):
        a, b, c = IL()
        arr.add(b)
    for node in range(1, n + 1):
        if node not in arr:
            for val in range(1, n + 1):
                if val != node:
                    print(node, val)
            return

for _ in range(II()):
    solve()
