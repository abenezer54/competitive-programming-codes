import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, q = IL()
    a = IL()
    queries = IL()
    ans = defaultdict(int)
    for i in range(n):
        x = n - i - 1
        y = i * (n - i)
        val = x + y
        ans[val] += 1
        nxt = val - i 
        if i < n - 1:
            d = a[i + 1] - a[i] - 1
            ans[nxt] += d
    
    res = [0] * q
    for i, k in enumerate(queries):
        if k in ans:
            res[i] = ans[k]
    print(*res)


    

for _ in range(II()):
    solve()
