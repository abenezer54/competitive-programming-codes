import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = IL()
    arr = [(a[i], i) for i in range(n)]
    arr.sort()
    p = [0] * n
    p[0] = arr[0][0]
    # print(arr)
    for i in range(1, n):
        p[i] += p[i - 1] + arr[i][0]
    ans = []
    # print(arr)
    for i in range(1, n):
        if p[i - 1] >= arr[i][0]:
            ans.append(arr[i - 1][1] + 1)
        else:
            ans.clear()
    # print(ans)
    ans.append(arr[-1][1] + 1)
    ans.sort()
    print(len(ans))
    print(*ans)


for _ in range(II()):
    solve()
