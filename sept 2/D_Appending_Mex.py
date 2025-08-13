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
    av = set()
    for i in range(n):
        if a[i] == 0 or a[i] - 1 in av:
            av.add(a[i])
        else:
            print(i + 1)
            return
    
    print(-1)

solve()
