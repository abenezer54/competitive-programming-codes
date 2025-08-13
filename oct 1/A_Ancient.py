import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
# print((1 + (3/8) + (4/16) )* 16)
MOD = int(1e9) + 7
def solve():
    n = II()
    ans = pow(2, n + 1, MOD) - (n + 2)
    print(ans % MOD)    
    
    

for _ in range(II()):
    solve()
