import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    mat = [IL() for _ in range(n)]
    p = [0] * n
    for i in range(n):
        for j in range( m):
            if mat[i][j] % n != mat[i][0] % n:
                print(-1)
                return
            if mat[i][j] < n:
                p[mat[i][j]] = i + 1
    print(*p)
    
    
    


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()