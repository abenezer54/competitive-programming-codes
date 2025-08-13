import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
# print(1 << 59 > int(1e18))
def range_bitwise_and(l, r):
    shift_count = 0
    while l < r:
        l >>= 1
        r >>= 1
        shift_count += 1
    return l << shift_count

def solve():
    n, x = IL()
    N = n
    st = n
    bits = set()

    for i in range(62):
        if x & (1 << i):
            if not (n & (1 << i)):
                print(-1)
                return
        else:
            if n & (1 << i):
                bits.add(i)
                for j in range(i + 1):
                    if n & (1 << j):
                        mask = (1 << 62) - 1
                        mask -= (1 << j)
                        n &= mask
    if bits:
        mx = max(bits) + 1
        for j in range(mx):
           if N & (1 << j):
                mask = (1 << 62) - 1
                mask -= (1 << j)
                N &= mask 
        N |= 1 << mx
    # print(bits)
    if range_bitwise_and(st, N) == x:
        print(N)
    else:
        print(-1)



tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()