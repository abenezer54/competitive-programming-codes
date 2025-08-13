import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    l, n, m = IL()
    a = IL()
    grid = [IL() for _ in range(n)]
    r, c = -1, -1
    for num in a:
        for i in range(n - 1, r, -1):
            for j in range(m - 1, c, -1):
                if grid[i][j] == 
    

for _ in range(II()):
    solve()
