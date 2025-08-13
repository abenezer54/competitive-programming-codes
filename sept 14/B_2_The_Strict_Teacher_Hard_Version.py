import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m, q = IL()
    a = sorted(IL())
    q = IL()
    ans = []
    for start in q:
        idx = bisect_left(a, start)

        if idx < m: 
            if a[idx] == start:
                ans.append(0)
            else:
                if idx == 0:
                    ans.append(a[0] - 1)
                else:
                    x, y = a[idx], a[idx - 1]
                    mid = (x + y) // 2
                    val = min(abs(x - mid), abs(y - mid))
                    ans.append(val)
        else:
            ans.append(n - a[-1])

    for val in ans:
        print(val)
        

for _ in range(II()):
    solve()
