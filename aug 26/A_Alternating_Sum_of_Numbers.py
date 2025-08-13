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
    ans = 0
    if n & 1:
        a.append(0)
    for i in range(0, len(a) - 1, 2):
        ans += a[i] - a[i + 1]
    print(ans)

for _ in range(II()):
    solve()
