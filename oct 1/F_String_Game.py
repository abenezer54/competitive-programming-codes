import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    t = S()
    p = S()
    a = IL()
    mp = {a[i] - 1:i for i in range(len(a))}
    def check(mid):    
        i, j = 0, 0
        while i < len(t) and j < len(p):
            if mp[i] < mid:
                i += 1
            else:
                if t[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
        return j == len(p)
    
    l, r = 0, len(a) + 1
    while l + 1 < r:
        mid = (l + r) // 2
        if check(mid):
            l = mid
        else:
            r = mid
    print(l)   


solve()
