import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, s = IL()
    a = IL()
    b = IL()
    x = [a[i] & b[i] for i in range(n)]
    if a[0] and (a[s - 1] == 1 or (x[s:].count(1) > 0 and b[s - 1] == 1)):
        print("YES")   
    else:
        print("NO")           
    

solve()
