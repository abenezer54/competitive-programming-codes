import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    s = S()
    l, r = 0, n - 1
    while l < r:
        # print(l, r)
        if s[l] == s[r]:
            l += 1
            r -= 1
        else: break
    if l > r:
        l -= 1

    if k  <= l:
        print("YES")
    else:
        print("NO")
for _ in range(II()):
    solve()
