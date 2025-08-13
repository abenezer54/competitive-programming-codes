import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    s = S()
    k = II()
    val = len(s) - len(set(s))
    tot = len(set(s)) + val
    if len(set(s)) >= k:
        print(0)
        return
    if tot < k:
        print("impossible")
        return
    print(k - len(set(s)))

solve()
