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
    vis = set()
    ans = []
    for i in range(2 * n):
        if a[i] not in vis:
            ans.append(a[i])
            vis.add(a[i])
    print(*ans)

for _ in range(II()):
    solve()
