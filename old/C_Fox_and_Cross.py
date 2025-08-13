import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    grid = [S() for _ in range(n)]
    cnt = Counter()
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if grid[i][j] == '#' and (i, j) not in cnt and grid[i - 1][j] == '#' and (i - 1, j) not in cnt  and grid[i + 1][j] == '#' and (i + 1, j) not in cnt  and grid[i][j - 1] == '#' and (i, j - 1) not in cnt and grid[i][j + 1] == '#' and (i, j + 1) not in cnt:
                cnt[(i, j)] += 1
                cnt[(i + 1, j)] += 1
                cnt[(i - 1, j)] += 1
                cnt[(i, j + 1)] += 1
                cnt[(i, j - 1)] += 1

    for i in range(n):
        for j in range(n):
            if grid[i][j] == '#' and (i, j) not in cnt:
                print("NO")
                return   
            
    if cnt and max(cnt.values()) > 1:
        print("NO")
    else:
        print("YES")



tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()