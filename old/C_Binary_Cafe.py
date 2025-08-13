import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
# print(1 << 6)
def solve():
    n, k = IL()
    b = bin(n)[2:]
    b = b[::-1]
    # print(b)
    ans = 0
    for i in range(len(b)):
        found = False
        for j in range(i + 1, len(b)):
            if b[j] == '1':
                found = True
        if found and (1 << i) <= n and i < k:
            ans += 1 << i
        elif not found and  (1<< i )<= n and i < k:
            for j in range(i):
                if b[j] == '1':
                    ans += 1 << j
            # print('here', mx)
            ans += 1

            # ans += 1 << min(mx, k)
    print(ans + 1)


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()