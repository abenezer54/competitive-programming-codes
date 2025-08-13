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
    odd = even = 0
    b = []
    for i in range(n - 1, -1, -1):
        if i & 1:
            val = a[i] + even - odd
            b.append(val)
            odd += val
        else:
            val = a[i] - even + odd
            b.append(val)
            even += val
        # print(i, even, odd)
    print(*b[::-1])
solve()
