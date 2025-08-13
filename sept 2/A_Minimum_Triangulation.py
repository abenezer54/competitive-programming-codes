import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    ans = 0
    cur = 2
    for i in range(n - 2):
        ans += cur * (cur + 1)
        cur += 1
    print(ans)
solve()
