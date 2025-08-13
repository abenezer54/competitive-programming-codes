import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, x, m = IL()
    left = right = x
    # print('prev', left, right)
    for _ in range(m):
        c, d = IL()
        if c <= left and d >= right:
            # print('first', c, d)
            left = min(c, left)
            right = max(right, d)
        elif c <= right and c >= left:
            # print('mid', c, d)
            left = min(c, left)
            right = max(right, d)
        elif d >= left and d <= right:
            # print('last', c, d)

            left = min(c, left)
            right = max(right, d)
    print(right - left + 1)

for _ in range(II()):
    solve()
