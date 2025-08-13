import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    s, t = S().split()
    s = list(s)
    t = list(t)
    # print(t)
    vis = set()
    n, m = len(s), len(t)
    i, j = n-1, m-1
    while i >= 0 and j >= 0:
        if s[i] == t[j]:
            j -= 1
            vis.add(i)
            # print(s[i])
        i -= 1
    if j != -1:
        print("NO")
        return
    for idx in vis:
        for i in range(idx + 1, n):
            if s[idx] == s[i] and i not in vis:
                print("NO")
                return
    print("YES")

for _ in range(II()):
    solve()
