import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    p = S()
    s = S()

    ans = 0
    for i in range(len(s) - 1):
        ans += abs(p.index(s[i]) - p.index(s[i + 1]))
    print(ans)

for _ in range(II()):
    solve()
