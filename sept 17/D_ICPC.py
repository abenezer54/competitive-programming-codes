import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def find_divisors(number):
    divisors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    return divisors
def solve():
    n = II()
    u = IL()
    s = IL()
    uni = defaultdict(list)
    ans = [0] * n
    vis = defaultdict(set)
    for i in range(n):
        uni[u[i]].append(s[i])
    for cur_uni, arr in uni.items():
        arr.sort(reverse=True)
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        for i in range(len(arr), 0, -1):
            div = find_divisors(i)
            for d in div:
                if d not in vis[cur_uni]:
                    vis[cur_uni].add(d)
                    ans[d - 1] += arr[i - 1]

    print(*ans)
    # print(uni)




for _ in range(II()):
    solve()
