import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a  = IL()
    b = IL()
    if n <= 2:
        print("Bob")
        return
    r = a[::-1]

    if a == b or r == b:
        print("Bob")
    else:
        print("Alice")

for _ in range(II()):
    solve()
