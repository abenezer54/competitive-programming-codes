import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    k = II()
    l = II()
    m = II()
    n = II()
    d = II()
    ans = set()
    for num in range(1, d + 1):
        if num % k == 0 or num % l == 0 or num % m == 0 or num % n == 0:
            ans.add(num)
    print(len(ans))
solve()
