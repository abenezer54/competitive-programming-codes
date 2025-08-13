import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    points = []
    for _ in range(n):
        points.append(IL())
    s = set()
    grid = [[0 for _ in range(2009)] for _ in range(2009)]
    for x, y in points:
        x += 1000
        y += 1000
        grid[x][y] = 1
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            x, y = points[i][0], points[i][1]
            r, c = points[j][0], points[j][1]
            mx, my = (x + r) / 2, (y + c) / 2
            if mx != int(mx) or my != int(my):
                  continue
            
            mx += 1000
            my += 1000
            if grid[int(mx)][int(my)] == 1:
                ans += 1

           
    print(ans)

    

solve()
