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
    b = IL()
    mn = min(a)
    mnb = min(b)
    ans = 0
    for i in range(n):
        v = v2 = 0
        if a[i] > mn:
            v = a[i] - mn
        if b[i] > mnb:
            v2 = b[i] - mnb
        m = min(v, v2)
        ans += m
        ans += max(v, v2) - m
    
    print(ans)
        

for _ in range(II()):
    solve()
