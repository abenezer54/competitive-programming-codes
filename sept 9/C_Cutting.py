import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()


def solve():
    n, b = IL()
    a = IL()
    cnt = 0
    arr = []
    for i in range(n - 1):
        if a[i] % 2== 0:
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            arr.append(abs(a[i] - a[i + 1]))
    arr.sort(reverse=True)
    ans = 0
    # print(arr)
    while arr and arr[-1] <= b:
        b -= arr.pop()
        ans += 1
    print(ans)


solve()
