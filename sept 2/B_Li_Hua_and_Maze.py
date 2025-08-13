import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    a, b, x, y = IL()
    def isc(i, j): return (i == 1 or i == n) and (j == 1 or j == m)
    if isc(a, b) or isc(x,y):
        print(2)
        return
    z = [1, n]
    k = [1, m]
    if (a in z) or (b in k) or (x in z) or (y in k):
        print(3)
        return
    print(4)
    

for _ in range(II()):
    solve()
