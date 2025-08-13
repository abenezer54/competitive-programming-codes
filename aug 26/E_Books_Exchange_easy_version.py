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
    ans = []
    for i in range(n):
        idx = a[i]
        cnt = 0
        while idx != i + 1:
            idx = a[idx - 1]
            cnt += 1
        ans.append(cnt + 1)
    print(*ans)

for _ in range(II()):
    solve()
