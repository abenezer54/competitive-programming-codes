import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    s = S()
    cp = s[:]
    n = len(s)
    q = IL()[0]
    a = IL()
    # print(a)
    ans = []
    for i in range(q):
        d = (a[i]) // n
        r = (a[i]) % n
        if d & 1:
            ans.append(s[r].swapcase())
        else:
            ans.append(s[r])
    for i in range(10):
        for i in range(0, len(s), 2):
            if s[i:i + 2] == cp:
                print('0', end=' ')
            else:
                print('r', end=' ')
            # print(s[i: i + 2], end=' ')
        print('\n')
        cur = s[:]
        print('cur', cur)
        for ch in cur:
            s += ch.swapcase()
        
    # print(*ans)

tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()