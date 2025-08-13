import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    grid = [IL() for _ in range(n)]
    cols = defaultdict(set)
    for i in range(n):
        for j in range(n):
            cols[j].add(grid[i][j])
    
    for i in range(n):
        for j in range(n):
            val = grid[i][j]
            if val > 1:
                found  = False
                for c in range(n):
                    if grid[i][c] <= val:
                        if val - grid[i][c] in cols[j]:
                            found = True
                if not found:
                    print("No")
                    return
    print("Yes")


solve()
