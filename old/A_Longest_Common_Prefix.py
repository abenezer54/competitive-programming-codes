import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    s = [S() for _ in range(n)]
    i = 0 
    while i < len(s[0]):
        cur = set()
        for word in s:
            cur.add(word[i])
        if len(cur) == 1:
            i += 1
        else:
            break
    print(i)


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()