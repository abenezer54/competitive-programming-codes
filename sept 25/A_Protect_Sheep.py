import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    grid = [list(S()) for _ in range(n)]
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def inb(i, j): return 0 <= i < n and 0 <= j < m
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                for x, y in d:
                    ni, nj = i + x, j + y
                    if inb(ni, nj):
                        if grid[ni][nj] == "W":
                            print("No")
                            return
                        elif grid[ni][nj] == ".":
                            grid[ni][nj] = "D"
    print("Yes")
    for row in grid:
        print(''.join(row))




solve()
