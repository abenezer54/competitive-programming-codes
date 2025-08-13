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
    left, mid, right = defaultdict(int), defaultdict(int), defaultdict(int)
    for i in range(n - 2):
        left[(a[i + 1], a[i + 2])] += 1
        left[(a[i + 1], a[i + 2], a[i])] += 1
    
        mid[(a[i], a[i + 2])] += 1
        mid[(a[i], a[i + 2], a[i + 1])] += 1

        right[(a[i], a[i + 1])] += 1
        right[(a[i], a[i + 1], a[i + 2])] += 1
    ans = 0
    for i in range(n - 2):
        ans += left[(a[i + 1], a[i + 2])] - left[(a[i + 1], a[i + 2], a[i])]
        ans += mid[(a[i], a[i + 2])] - mid[(a[i], a[i + 2], a[i + 1])]
        ans += right[(a[i], a[i + 1])] - right[(a[i], a[i + 1], a[i + 2])]
    print(ans // 2)

for _ in range(II()):
    solve()
