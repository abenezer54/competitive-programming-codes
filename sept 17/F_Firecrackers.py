import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
que = deque(["1", "0", "1"])
que.appendleft('1')
print(''.join(que))
def solve():
    n, m, a, b= IL()
    if a < b:
        tot = b - 1
    else:
        tot = n - b 
    diff = abs(a - b) - 1
    arr = sorted(IL(), reverse=True)
    # print(tot, diff)
    while arr and arr[-1] <= tot:
        tot -= arr.pop()
    print(m - min(diff, len(arr)))


for _ in range(II()):
    solve()
