import sys
from decimal import Decimal, getcontext
from math import sqrt

def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    arr = []
    for _ in range(n):
        arr.append(IL())
    
    a, b, x, y = IL()
    a, b, x, y = Decimal(a), Decimal(b), Decimal(x), Decimal(y)
    
    d = (a - x) ** 2 + (b - y) ** 2
    d = d.sqrt()

    for a, b in arr:
        a, b = Decimal(a), Decimal(b)
        dd = (a - x) ** 2 + (b - y) ** 2
        dd = dd.sqrt()   
        if dd <= d:
            print("NO")
            return
    print("YES")

for _ in range(II()):
    solve()
