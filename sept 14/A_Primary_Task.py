import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    s = S()
    if len(s) < 3:
        print("NO")
        return
    if s[:2] != '10':
        print("NO")
        return
    if int(s[2:]) < 2 or s[2] == '0':
        print("NO")
        return
    print("YES")

for _ in range(II()):
    solve()
