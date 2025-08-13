import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def find_divisors(number):
    divisors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    return sorted(divisors)    
def solve():
    a = II()
    inverse = 0
    if a.bit_length() == a.bit_count():
        ans = find_divisors(a)[-2]
        print(ans)
        return
    for i in range(a.bit_length()):
        if not (a & (1 << i)):
            inverse |= (1 << i)
    print(math.gcd(a ^ inverse, a & inverse))
    

for _ in range(II()):
    solve()
