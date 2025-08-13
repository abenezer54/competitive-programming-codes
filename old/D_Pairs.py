import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    a = []
    for _ in range(m):
        a.append(IL())
    prev = [[a[0][0]],[a[0][1]]]

    for i in range(1, m):
        cur = []
        for arr in prev:
            if a[i][0] in arr or a[i][1] in arr:
                cur.append(arr)
            else:
                if len(arr) == 1:
                    cur.append(arr + [a[i][0]])
                    cur.append(arr + [a[i][1]])
        prev = cur
        
    if prev:
        print("YES")
    else:
        print("NO")

tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()