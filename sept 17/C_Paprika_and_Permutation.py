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
    # print(a)
    # print(a)
    ans = 0
    for i in range(n):
        if a[i] == i + 1:
            continue
        
        if a[i] < i + 1:
            print(-1)
            return
        d = a[i] - (i + 1) 
        if d <= 0:
            print(-1)
            return
        if a[i] % d != i + 1:
            print(-1)
            return
        ans += 1
    print(ans)
for _ in range(II()):
    solve()
