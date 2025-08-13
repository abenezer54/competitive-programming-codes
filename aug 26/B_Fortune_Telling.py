import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, x, y = IL()
    a = IL()
    if (sum(a) ^ x ^ y) & 1:
        print("Bob")
        return 
    print("Alice")

for _ in range(II()):
    solve()
