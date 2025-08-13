import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = IL()
    a.sort()
    a = sorted(list(set(a)))
    if len(a) != n :
        print("NO")
        return
    print(a)
    for i in range(1, len(a)):
        
        if (a[i] - a[i - 1])% ((n *2) - 4 )!= 0:
            print(a[i], a[i - 1])
            print("NO")
            return
    print("YES")
for _ in range(II()):
    solve()
