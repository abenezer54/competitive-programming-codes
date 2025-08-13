import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    # if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n != 1:
    #     print(-1)
    #     return
    cnt = 0
    while n != 1:
        if n % 2 == 0:
            n = n //  2
        elif n % 3 == 0:
            n = (n // 3) * 2
        elif n % 5 == 0:
            n = (n // 5) * 4
        else:
            print(-1)
            return
        cnt += 1
    print(cnt)


for _ in range(II()):
    solve()
