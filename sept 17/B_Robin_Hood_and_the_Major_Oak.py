import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    if n % 2 == 0:
        even = (k //2)
        odd = (k //2) 
        if k & 1:
            even += 1

    else:
        odd = (k //2)
        even = (k //2)  
        if k & 1:
            odd += 1
    if odd % 2 == 0:
        print("YES")
    else:
        # print(odd, even)
        print("NO")

for _ in range(II()):
    solve()
