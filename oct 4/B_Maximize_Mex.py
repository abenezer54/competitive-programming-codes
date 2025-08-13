import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, x = IL()
    a = sorted(IL())
    # print(a)
    cnt = Counter()
    idx = 0
    for num in  range(int(1e6)):
        while idx < n and a[idx] <= num:
            cnt[a[idx]%x] += 1
            idx += 1 
        need = (num // x) + 1
        if need > cnt[num % x]:
            print(num)
            return


for _ in range(II()):
    solve()
