import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    ran = random.randint(1000, 100000000)
    k = IL()[0]
    a = IL()
    check = set()
    for num in a:
        check.add(num ^ ran)
    k -= 2
    for i in range(1, k + 1):
        x = i
        y = k // i
        r = k % i
        if r == 0 and (x ^ ran) in check and (y ^ ran) in check:
            print(x, y)
            return
    

tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()