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
    a.reverse()
    k = a.count(1)
    # print(k)
    ans = 0
    for i in range(k):
        if a[i] == 0:
            ans += 1
    print(ans)
for _ in range(II()):
    solve()
