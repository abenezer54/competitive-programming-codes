import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    s = S()
    ans = []
    for char in s:
        if char == 'w':
            ans.append('w')
        elif char == 'p':
            ans.append("q")
        else:
            ans.append('p')
    ans.reverse()
    print("".join(ans))

tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()