import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    s, h, n = IL()
    a = IL()
    b = IL()
    arr = [(a[i], b[i]) for i in range(n)]
    tot = 0
    arr.sort()
    for i in range(n):
        need = ceil(arr[i][1] / s)
        if i == n - 1:
            need -= 1
        tot += need * arr[i][0]
        
    if tot < h:
        print("YES")      
    else:
        print("NO")      

for _ in range(II()):
    solve()
