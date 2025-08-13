import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
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
    return is_prime
primes = prime_sieve(int(1e6))

# from itertools import permutations
# print(list(permutations(list(range(1, 5)))))
def solve():
    n = IL()[0]
    if n < 5:
        print(-1)
        return
    if n == 5:
        print(2, 4, 5, 1, 3)
        return
    ans = []
    for num in range(1, n + 1):
        if not (num & 1):
            ans.append(num)
    val = -1
    for num in range(1, n + 1, 2):
        if not primes[num + ans[-1]]:
            # print(num + ans[-1])
            ans.append(num)
            val = num
            break
    for num in range(1, n + 1):
        if num & 1 and num != val:
            ans.append(num)

    print(*ans)        



tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()