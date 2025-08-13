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
    home = True
    ans = 0
    for i in range(n):
        if a[i] == 1:
            home = False
        else:
            if i > 0 and a[i - 1] == 0:
                if not home:
                    ans -= 1
                home = True
            if i == n - 1:
                home = True
        if not home:
            ans += 1
    print(ans)

solve()
