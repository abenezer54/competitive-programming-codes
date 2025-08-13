import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    cur = 0
    n, k = IL()
    a = IL()
    ans = 0
    for i in range(n):
        if a[i] >= k:
            cur += a[i]
        
        if a[i] == 0 and cur >0:
            ans += 1
            cur -= 1
    print(ans)

    

for _ in range(II()):
    solve()
