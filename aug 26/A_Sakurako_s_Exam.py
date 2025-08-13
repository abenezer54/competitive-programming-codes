import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    a, b = IL()
    a -= 2 * (b % 2)
    if a >= 0 and a % 2 == 0:
        print("YES")
    else:
        print("NO")


for _ in range(II()):
    solve()
