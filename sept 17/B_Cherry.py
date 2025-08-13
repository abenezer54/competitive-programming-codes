import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = IL()
    ans = -float('inf')
    for i in range(n - 1):
        val = max(a[i], a[i + 1]) * min(a[i], a[i + 1])
        ans = max(ans,val)
    print(ans)

for _ in range(II()):
    solve()
