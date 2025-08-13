import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    ans = math.ceil(k /2)
    if k == (n * 4) - 2:
        ans += 1
    print(ans)

for _ in range(II()):
    solve()
