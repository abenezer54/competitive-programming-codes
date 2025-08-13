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
    # print(a)
    # print(b)
    i = j = 0
    vis = set()
    ans = 0
    while i < n:
        if a[i] in vis:
            i += 1
            continue
        
        while j < n and b[j] != a[i]:
            ans = j + 1
            vis.add(b[j])
            j += 1

        i += 1
        j += 1
    a = [1, 2, 2,2,3,5]
    print(a)
    print(bisect_left(a, 4))
    print(ans)
            




for _ in range(II()):
    solve()
