import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    s = 'aeiou'
    ans = ''
    x = n // 5
    r = n % 5
    for i in range(5):
        val = s[i] * x
        if r > 0:
            val += s[i]
            r -= 1
        ans += val
    print(ans)

for _ in range(II()):
    solve()
