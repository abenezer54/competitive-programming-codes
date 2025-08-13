import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = IL()
    neg, zero, pos = [], [],  []
    # print(a)
    for val in a:
        if val < 0:
            neg.append(val)
        elif val > 0:
            pos.append(val)
        else:
            zero.append(val)
    # print(neg, zero, pos)
    if len(neg) % 2 == 0:
        zero.append(neg.pop())
    
    if len(pos) == 0:
        pos.append(neg.pop())
        pos.append(neg.pop())

    
    
    print(len(neg), *neg)
    print(len(pos), *pos)
    print(len(zero), *zero)


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()