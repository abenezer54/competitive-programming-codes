import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    s = S()
    ans = []
    cnt = Counter(s)
    temp = []
    for k, v in cnt.items():
        temp.append((v, k))
    print(temp)
for _ in range(II()):
    solve()
