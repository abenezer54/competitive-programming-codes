import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    a, b, p = IL()
    s = S()
    n = len(s)
    arr = [0] * n
    for i in range(n - 2, -1, -1):
        if i == n - 2:
            arr[i] = a if s[i] == "A" else b
        elif s[i] != s[i + 1]:
            val = a if s[i] == "A" else b
            arr[i] = arr[i + 1] + val
        else:
            arr[i] = arr[i + 1]
    # print(arr)
    for i in range(n):
        if arr[i] <= p:
            print(i + 1)
            return

for _ in range(II()):
    solve()
