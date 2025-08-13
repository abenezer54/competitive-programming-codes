import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
my_list = [[0] for _ in range(5)] 
my_list[0][0] = 8
print(my_list)
def solve():
    n, k = IL()
    a = IL()
    arr = []
    for i in range(1, n):
        arr.append(abs(a[i] - a[i - 1]))
    arr.sort(reverse=True)
    ans = sum(arr)
    # print(arr)
    for i in range(k - 1):
        ans -= arr[i]
    print(ans)


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()