import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    x, y = IL()
    sx, sy = str(x), str(y)
    ans = 0
    k = 0
    if sx[0] <= sy[0]:
        ans += 1
        k += x * pow(10, len(sy)-len(sx))
        y -= k
        while x <= y:
            y -= x
            ans += 1
        ans += y
        print(ans)
    else:
        val = x * pow(10, len(sy)- len(sx) - 1)
        k += y // val
        y -= k * val
        ans += k
        while x <= y:
            y -= x
            ans += 1
        ans += y
        print(ans)

        
   


for _ in range(II()):
    solve()
