import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
# print((1 << 30) > int(1e9))

def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    return prime
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
    return factors

def find_divisors(number):
    divisors = []
    limit = int(number**0.5) + 1
    for i in range(1, limit):
        if number % i == 0:
            divisors.append(i)
            complement = number // i
            if i != complement:
                divisors.append(complement)
    return divisors
def solve():
    n = IL()[0]
    a = IL()
    mx = a[0]
    ans = 0
    flag = True
    for i in range(1, n):
        while flag and a[i] < mx:
            a[i] <<= 1
            ans += 1
        while not flag  and a[i] < (1 << 30):
            ans += 1

        if a[i] > int(1e9):
            flag = False
        mx = max(mx, a[i])
    print(ans)
        


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()