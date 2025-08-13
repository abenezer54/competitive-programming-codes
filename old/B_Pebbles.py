import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def find_divisors(number):
    divisors = []
    limit = int(number**0.5) + 1
    for i in range(1, limit):
        if number % i == 0:
            divisors.append(i)
            complement = number // i
            if i != complement:
                divisors.append(complement)
    return sorted(divisors)

def solve():
    n = IL()[0]
    ans = 0
    cnt = 0
    while n != 1:
        ans += n
        d = find_divisors(n)
        n = n // d[1]

    print(ans + 1)
    


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()