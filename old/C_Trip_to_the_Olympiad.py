import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    return prime
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
    pass


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()