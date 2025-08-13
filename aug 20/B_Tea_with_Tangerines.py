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
    val = min(a) * 2
    ans  = 0
    # print('val', val)
    for i in range(n):
        if a[i] >= val:
            ans += ceil(a[i] / (val - 1)) - 1

    print(ans)


for _ in range(II()):
    solve()
