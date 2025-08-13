import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
print
def solve():
    n, k = IL()
    a = [II() for _ in range(n)]
    def check(mid):
        cnt = 0
        for num in a:
            cnt += num // mid
        return cnt >= k

    l, r = 1e-6, 1e8
    while l + 1e-6 < r:
        mid = (l + r) / 2
        if check(mid):
            l = mid
        else:
            r = mid
    print(l)




solve()
