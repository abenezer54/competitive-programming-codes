import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    s = S()
    ans = 0
    zero = 0
    one = 0
    for i in range(len(s)):
        if zero:
            if s[i] == '1':
                ans += 1
                zero -= 1
            else:
                zero += 1
        elif one:
            if s[i] == '0':
                ans += 1
                one -= 1
            else:
                one += 1
        else:
            if s[i] == '0':
                zero += 1
            else:
                one += 1
    

        
    if ans & 1:
        print("DA")
    else:
        print("NET")


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()