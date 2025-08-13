import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    s = S()
    n = len(s)
    for r in range(n - 1):
        for l in range(0, r + 1):
            left = s[: r + 1]
            right = s[l:]
            if left == right:
                # print(r, l)
                print("YES")
                print(left)
                return
    print("NO")

solve()
