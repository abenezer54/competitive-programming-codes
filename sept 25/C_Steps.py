import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    i, j = IL()
    k = II()
    a = [IL() for _ in range(k)]
    cnt = 0
    for dx, dy in a:
        x = y = 0
        if dx > 0:
            possx = n - i
            x = possx // dx
        elif dx < 0:
            possx = i - 1
            x = possx // abs(dx)
        else:
            x = float('inf')
        # print('top', dx, x)
        if dy > 0:
            possy = m - j
            y = possy // dy
        elif dy < 0:
            possy = j - 1
            y = possy // abs(dy)
        else:
            y = float('inf')
        x = max(0, x)
        y = max(0, y)

        z = min(x, y)
        i += (z * dx)
        j += (z * dy)
        cnt += z
        # print(cnt)
    print(cnt)


         
    

solve()
