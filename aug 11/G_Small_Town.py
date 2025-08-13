import sys
import decimal
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = IL()
    a = sorted(list(set(a)))
    n = len(a)
    if n <= 3:
        print(0)
        return

    def check(mid):
        cnt = 1
        mn = a[0]
        for i in range(n):
            if (a[i] - mn) / 2 > mid:
                cnt += 1
                mn = a[i]
            # print(mn)
        return cnt
    # print(check(2))
    l, r = 0, max(a) // 3
    while l + 1 < r:
        mid = (l + r) // 2
        if check(mid) <= 3:
            r = mid
        else:
            l = mid
    print(r)
        



for _ in range(II()):
    solve()
