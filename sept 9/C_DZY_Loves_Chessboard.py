import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
import math
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
print((6 * (6 - 1)) // 2)

def solve():
    n, m = IL()
    grid = [S() for _ in range(n)]
    ans = [["-"] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.': 
                if i % 2 == 0:
                    if j % 2 == 0:
                        ans[i][j] = "B"
                    else:
                        ans[i][j] = "W"
                else:
                    if j % 2 == 0:
                        ans[i][j] = "W"
                    else:
                        ans[i][j] = "B"

    # print(ans)
    for row in ans:
        print(''.join(row))
                


solve()
