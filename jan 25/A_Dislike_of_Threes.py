import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    k = IL()[0]
    cnt = 0
    for num in range(1, int(1e6)):
        if num % 3 == 0 or str(num)[-1] == '3':
            continue
        cnt += 1
        if cnt == k:
            print(num)
            return
        


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()