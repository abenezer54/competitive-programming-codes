import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = IL()
    cnt = 0
    mx = max(a)
    cur = 0
    for i in range(n - 1, -1, -1):
        if a[i] == mx:
            break
        if a[i] > cur:
            cnt += 1
            cur = a[i]
    print(cnt)
for _ in range(II()):
    solve()
