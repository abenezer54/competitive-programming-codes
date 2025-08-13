import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    a = IL()
    def check(mid):
        if max(a) > mid:
            return False
        sm = cnt = 0
        for i in range(n):
            sm += a[i]
            if sm > mid:
                sm = a[i]
                cnt += 1
        cnt += 1
        return cnt <= k

    l, r = 0, int(1e18)
    while l + 1 < r:
        mid = (l + r)//2
        if check(mid):
            r = mid
        else:
            l = mid
    print(r)  
    

solve()
