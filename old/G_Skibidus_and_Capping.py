import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def find_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i 
        i += 1
    if n > 1: 
        factors.append(n)
    return sorted(factors)

def solve():
    
    n = IL()[0]
    a = IL()
    mp = Counter()
    one = Counter()
    third = Counter()
    for val in a:
        f = find_prime_factors(val)
        if len(f) > 2:
            continue
        if (len(f)) == 2:
            mp[tuple(f)] += 1
            third[f[0]] += 1
            if f[1] != f[0]:
                third[f[1]] += 1
        else:
            one[f[0]] += 1

    ans = 0
    o = 0
    tot = sum([val for val in one.values()]) if one else 0
    for key, val in one.items():
        cur = tot - val
        o += cur * val 
        ans += val * third[key]

    ans += o // 2
    for val in mp.values():
        ans += (val * (val + 1)) // 2
    
    print(ans)
    
    



tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()