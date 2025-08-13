import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def prime_sieve(n):
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = is_prime[1] = False
    i = 2
    while i * i <= n:
        if is_prime[i]:
            j = i * i
            while j <= n:
                is_prime[j] = False
                j += i
        i += 1
    primes = []
    for i in range(n + 1):
        if is_prime[i]:
            primes.append(i)
    return primes
primes = prime_sieve(5 * 10000)
def solve():
    d = II()
    x = 1
    y = primes[bisect_left(primes, x + d)]
    z = primes[bisect_left(primes, y + d)]
    print(y * z)

for _ in range(II()):
    solve()
