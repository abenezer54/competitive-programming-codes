import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    s = S()
    if n == 1:
        print('YES')
        return
    found = False
    for i in range(n):
        if s[i] == 'p':
            found = True
        if s[i] == 's':
            if found:
                print("NO")
                return
            
    s = s[1: -1]
    if s.count('p') and s.count('s'):
        print("NO")
        return
    print("YES")


tt = IL()[0]
for _ in range(tt):
    solve()