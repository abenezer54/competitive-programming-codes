import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m, k = IL()
    a = IL()
    if n == 1:
        print("YES")
        return
    # print(a)
    for i in range(1, n):
        mn = max(0, a[i] - k)
        if a[i - 1] >= mn:
            m += a[i - 1] - mn
        else:
            diff = mn - a[i - 1]
            if m < diff:
                print("NO")
                return
            m -= diff
        # print(i, m)
    print("YES")

for _ in range(II()):
    solve()
