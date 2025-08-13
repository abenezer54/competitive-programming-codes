import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    if n == 2:
        print(-1)
        return
    ans = [[0] * n for _ in range(n)]
    a, b = 1, pow(n, 2)
    cnt = 0
    mutex = 0
    for i in range(n):
        for j in range(n):
            if mutex == 0:
                ans[i][j] = a + cnt
            else:
                ans[i][j] = b - cnt
            cnt += 1
            mutex = 1 - mutex
    for row in ans:
        print(row)



for _ in range(II()):
    solve()
