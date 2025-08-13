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
        left, cnt = 0, 1
        for right in range(1, n):
            if a[right] - a[left] >= mid:
                cnt += 1
                left = right
        return cnt >= k

    l, r = 0, int(1e18)
    while l + 1 < r:
        mid = (l + r)//2
        if check(mid):
            l = mid
        else:
            r = mid
    print(l)

solve()
