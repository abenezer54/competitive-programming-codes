import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m, k = IL()
    # print(1 // 6)
    r = ceil((k )/ (2 * m) ) - 1
    d = k - ((r) * (2 * m))
    # print(d)
    ans = "L" if  d % 2 else "R"
    d = ceil(d / 2) - 1
    print(r + 1, d + 1, ans)

solve()
