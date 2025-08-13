import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    b, c, d = IL()
    mp = defaultdict(list)
    mp[(0, 0)] = [0, 1]
    mp[(0, 1)] = [0]
    mp[(1, 0)] = [1, 1]
    mp[(1, 1)] = [1, 0]
    ans = 0
    for bit in range(62):
        x = 1 if b & (1 << bit) else 0
        y = 1 if c & (1 << bit) else 0
        target = 1 if d & (1 << bit) else 0
        if x != y and target !=  x:
            print(-1)
            return
        ans |= (mp[(x, y)][target] << bit)
    print(ans)
    

for _ in range(II()):
    solve()
