import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    invalid = set([1, 2, 3, 5, 7, 11])
    ans = {4:1, 6:1, 8:2, 9:1, 10:2,12:3, 13:2, 14:3, 15:2}
    arr = [3, 2,3, 2]
    n = IL()[0]
    if n in invalid:
        print(-1)
    else:
        if n in ans:
            print(ans[n])
        else:
            n -= 12
            d = n// 4
            r = n % 4
            print(arr[r] + d)



tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()