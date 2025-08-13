import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    s = S()
    a = []
    left = -1
    for i in range(n):
        if s[i] == '1' and (i == 0  or s[i - 1] == '0'):
            left = i
        if s[i] == '1' and (i == n - 1 or s[i + 1] == '0'):
            a.append((left, i))
    left, right = a[k - 1][0], a[k - 1][1]
    ln = right - left + 1
    ans = []
    # print(a[k - 2][1])
    for i in range(a[k - 2][1] + 1):
        ans.append(s[i])
    ans.extend(['1'] * ln)
    for i in range(a[k-2][1] + 1, n):
        if not (left <= i <= right):
            ans.append(s[i])
    print(''.join(ans))


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()