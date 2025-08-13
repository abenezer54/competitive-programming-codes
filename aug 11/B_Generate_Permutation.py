import math
import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    # print(math.sqrt(1000))
    n = II()
    if n % 2 == 0:
        print(-1)
        return
    if n == 1:
        print(1)
        return
    ans = deque([n])
    n -= 1
    while n > 0:
        if n & 1:
            ans.appendleft(n)
        else:
            ans.append(n)
        n -= 1
    print(*ans)


for _ in range(II()):
    solve()
