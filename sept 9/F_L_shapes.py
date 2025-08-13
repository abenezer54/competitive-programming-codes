import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    grid = [S() for _ in range(n)]
    side = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    edge = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
    def inbound(i, j): return (0 <= i < n) and (0 <= j < m)

    vis = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*' and vis[i][j] == 0:
                vis[i][j] = 1
                cnt = 0
                flag = True
                stack = [(i, j)]
                row = Counter()
                col = Counter()
                diagonals = set()
                tot = set()
                while stack:
                    # print(stack)
                    tot.add(stack[-1])
                    cnt += 1
                    x, y = stack.pop()
                    row[x] += 1
                    col[y] += 1
                    for r, c in side:
                        ni, nj = x + r, y + c
                        if inbound(ni, nj) and vis[ni][nj] == 0 and grid[ni][nj] == '*':
                            vis[ni][nj] = 1
                            stack.append((ni, nj))
                    edgecnt = 0
                    for r, c in edge:
                        ni, nj = x + r, y + c
                        if inbound(ni, nj) and grid[ni][nj] == '*':
                            diagonals.add((ni, nj))
                # print(cnt)
                if cnt != 3 :
                    flag = False    
                # print(row, col, flag)
                if len(row) != 2 or len(col) != 2:
                    flag = False
                if not flag:
                    print("NO")
                    return
                temp = sorted([val for val in row.values()])
                temp2 = sorted([val for val in col.values()])
                if temp[0] != 1 or temp[1] != 2:
                    flag = False
                if temp2[0] != 1 or temp[1] != 2:
                    flag = False
                
                for val in diagonals:
                    if val not in tot:
                        flag = False
                        break
                if not flag:
                    print("NO")
                    return
    print("YES")
                    


for _ in range(II()):
    solve()
