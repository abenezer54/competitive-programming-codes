import heapq
import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m, d = IL()
    a = IL()
    heap = []
    ans = cur = 0
    for i in range(n):
        if a[i] > 0:
            cur += a[i]
            heapq.heappush(heap, a[i])
            if len(heap) > m:
                cur -= heapq.heappop(heap)
        ans = max(ans, cur - (d * (i + 1)))
    print(ans)

for _ in range(II()):
    solve()
