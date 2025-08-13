import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = sorted(IL())
    ans = 0
    for i in range(1, n):
        ans += a[i] - a[i - 1]
    print(ans)

for _ in range(II()):
    solve()
