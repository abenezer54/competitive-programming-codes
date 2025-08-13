import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    grid = [IL() for i in range(n)]
    prefix = []
    for i in range(n):
        cur = [0]
        for j in range(m):
            cur.append(cur[-1] + grid[i][j])
        prefix.append(cur)
    
    suffix = []
    for i in range(n):
        cur = [0]
        for j in range(m - 1, -1, -1):
            cur.append(cur[-1] + grid[i][j])
        suffix.append(cur[::-1])

    top = []
    for j in range(m):
        cur = [0]
        for i in range(n):
            cur.append(cur[-1] + grid[i][j])
        top.append(cur)
    
    buttom = []
    for j in range(m):
        cur = [0]
        for i in range(n -1, -1, -1):
            cur.append(cur[-1] + grid[i][j])
        buttom.append(cur[::-1])

    # print(top)
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                if prefix[i][j + 1]:
                    ans += 1
                if suffix[i][j]:
                    ans += 1
                if top[j][i + 1]:
                    ans += 1
                if buttom[j][i]:
                    ans += 1

                
    print(ans)

        

solve()
