import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    x1, y1 = IL()
    x2, y2 = IL()
    n = II()
    s = S()

    def check(mid):
        x, y = x1, y1
        r = mid % n
        d = mid // n
        # print(d, r)
        for i, char in enumerate(s):
            cur = d if i >= r  else d + 1
            if char == "U":
                y += cur 
            if char == "D":
                y -= cur
            if char == "L":
                x -= cur
            if char == "R":
                x += cur
        d = abs(x - x2) + abs(y - y2)
        return d <= mid
    
    INF = int(1e20)
    l, r = 0, INF
    # print(check(5))
    while l + 1 < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid
    if r == INF:
        print(-1)
    else:
        print(r)
    # check(5)
        

solve()
