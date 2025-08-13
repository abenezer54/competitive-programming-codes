import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a, b = 0, 0
    z = n
    while z % 2 == 0:
        z //= 2
        a += 1
        
    while z % 3 == 0:
        z //= 3
        b += 1
    
    if z != 1 or a > b: 
        print(-1)
        return
    # print(a, b)
    d = b - a
    print(d + b)
    
for _ in range(II()):
    solve()
