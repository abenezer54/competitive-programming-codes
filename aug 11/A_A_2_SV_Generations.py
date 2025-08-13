import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = sorted(IL())
    if n == 1:
        print(a[0])
    elif n == 3:
        print(a[1])
    else:
        print(a[2])
    a 

solve()
