import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    a = max(IL())
    if a == 1:
        print("1/1")
    else:
        b, c = 6 - a + 1, 6
        if c % 2 == 0 and b % 2 == 0:
            b //= 2
            c //= 2
        if c % 3 == 0 and b % 3 == 0:
            b //= 3
            c //= 3
        print(str(b) + "/" + str(c))


solve()
