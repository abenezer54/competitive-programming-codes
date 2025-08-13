import sys
import random
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = IL()
    r = random.randint(1000, 10000000000)
    check = set()
    for num in a:
        check.add(num ^ r)

    for num in a:
        for i in range(32):
            p = pow(2, i)
            val1 = (num - p) ^ r
            val2 = (num + p) ^ r
            if val1 in check and val2 in check:
                print(3)
                print(num, num - p, num + p)
                return
    for num in a:
        for i in range(32):
            p = pow(2, i)
            if (num - p )^ r in check:
                print(2)
                print(num, num - p)
                return
    print(1)
    print(a[0])
    

    


solve()
