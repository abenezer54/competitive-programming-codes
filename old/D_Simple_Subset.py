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
prime = sieve(3 * int(1e6))

def solve():
    n = IL()[0]
    a = IL()
    first = []

    for i in range(n):
        for j in range(i + 1, n):
            if a[i] != 1 and a[j] != 1:
                if prime[a[i] + a[j]]:
                    first = (a[i], a[j])
                    break
    
    second = [1] * a.count(1)
    for i in range(n):
        if a[i] != 1 and prime[a[i] + 1]:
            second.append(a[i])
            break

    ans = first if len(first) > len(second) else second
    if len(ans) == 0:
        ans = [a[0]]
        
    print(len(ans))
    print(*ans)




tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()