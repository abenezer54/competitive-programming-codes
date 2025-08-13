import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    s = list(S())
    if s[0] == s[-1]:
        s[1] = '='
    elif s[0] < s[-1]:
        s[1] = '<'
    else:
        s[1] = '>'
    print(''.join(s))


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()