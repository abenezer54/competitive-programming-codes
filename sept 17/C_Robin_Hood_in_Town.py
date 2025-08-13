import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = IL()
    mx = max(a)
    INF = int(1e18) + 10
    sm = sum(a)
    def check(mid):
        avg = sm + mid
        cnt = 0
        flag = False
        for i in range(n):
            if not flag:
                if a[i] == mx:
                    flag = True
                    continue
            if a[i] * n < avg / 2:
                cnt += 1
        return (cnt * 2) > n
    

    l, r = -1, INF
    while l + 1 < r:
        mid = (l + r) //2
        if check(mid):
            r = mid
        else:
            l = mid

    if r == INF:
        print(-1)
        return     
    print(r)
    

for _ in range(II()):
    solve()
