import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    prev = set()
    if n == 1:
        if sum(IL()) != 0:
            print("NO")
        else:
            print("YES")
        return
    
    for _ in range(n):
        cur = tuple(IL())

        for p in prev:
            sm = [0] * k
            for j in range(k):
                sm[j] += p[j]
                sm[j] += cur[j]
            if max(sm) < 2:
                print("YES")
                return
        prev.add(cur)
    print("NO")



tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()