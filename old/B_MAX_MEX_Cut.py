import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = S()
    b = S()
    ans = 0
    ok = [True] * (n)
    for i in range(n):
        if a[i] != b[i]:
            ans += 2
        else:
            if not ok[i]:
                continue
            if a[i] == '0':
                if i < n - 1 and a[i + 1] != a[i] and b[i + 1] != a[i]:
                    ans += 2
                    ok[i + 1] = False
                else:
                    ans += 1   
            else:
                if i < n - 1 and a[i + 1] != a[i] and b[i + 1] != a[i]:
                    ans += 2
                    ok[i + 1] = False
    print(ans)
            


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()