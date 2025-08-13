import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    a, b = IL()
    mn = min(a, b)
    mx = max(max(a, b), mn * 2)
    print(mx * mx)
    

for _ in range(II()):
    solve()
