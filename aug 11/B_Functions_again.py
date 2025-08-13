import sys
import heapq
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = IL()
    d = []
    for i in range(n - 1):
        d.append(abs(a[i] - a[i + 1]))
    # print(d)
    even = d[:]
    if len(d) & 1:
        even.append(0)
    odd = d[1:]
    if len(odd) & 1:
        odd.append(0)
    
    ans = 0
    prev = 0
    for i in range(0, len(even) - 1, 2):
        cur = even[i] - even[i + 1]
        if prev + cur < 0:
            prev = 0
        else:
            prev += cur
        ans = max(ans, prev + even[i + 1])
    prev = 0
    for i in range(0, len(odd) - 1, 2):
        cur = odd[i] - odd[i + 1]
        if prev + cur < 0:
            prev = 0
        else:
            prev += cur
        ans = max(ans, prev + odd[i + 1])
    print(ans)

solve()
