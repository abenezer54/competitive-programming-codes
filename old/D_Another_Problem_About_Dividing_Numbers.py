import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def primeFactors(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(int(n))
    return primfac


def solve():
    a, b, k = IL()
    ran = random.randint(1000, 1000000000)
    x = primeFactors(a)
    y = primeFactors(b)
    ca = Counter()
    cb = Counter()
    for val in x:
        ca[val ^ ran] += 1
    for val in y:
        cb[val ^ ran] += 1

    seen = set()
    need = 0
    aa = bb = 0
    for key, val in ca.items():
        if key ^ ran not in seen:
            seen.add(key ^ ran)
            w = val
            z = cb[key]
            if w != z:
                need += 1
                diff = max(w, z) - min(w, z)
                if max(w, z) == w:
                    aa += diff
                else:
                    bb += diff
        
    for key, val in cb.items():
        if key ^ ran not in seen:
            seen.add(key ^ ran)
            w = val
            z = ca[key]
            if w != z:
                need += 1
                diff = max(w, z) - min(w, z)
                if max(w, z) == w:
                    bb += diff
                else:
                    aa += diff
    # if a == 1000000000:
    #     print(ca, cb)

    tot = 0
    if aa:
        tot += 1
    if bb:
        tot += 1
    # print(need, tot)

    if  k < tot or k > len(x) + len(y):
        print("NO")
        return
    # print(tot)
    if tot == 0 and k == 1:
        print("NO")
        return

    print("YES")
        
            
tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()