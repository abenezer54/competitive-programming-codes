import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    s = S()
    ans = float('inf')
    for i in range(26):
        ch = chr(97 + i)
        cost = 0
        l, r = 0, n - 1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if s[l] == ch:
                    cost += 1
                    l += 1
                elif s[r] == ch:
                    cost += 1
                    r -= 1
                else:
                    break
        if l > r:
            ans = min(ans, cost)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
        
        

tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()