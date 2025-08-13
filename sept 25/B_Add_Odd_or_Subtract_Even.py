import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    a, b = IL()
    aa, bb = a % 2, b % 2
    if a == b:
        print(0)
        return
    if a < b:
        if aa == bb:
            print(2)
        else:
            print(1)
    else:
        if aa == bb:
            print(1)
        else:
            print(2)



for _ in range(II()):
    solve()
