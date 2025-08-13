import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m, q = IL()
    a = IL()
    b = IL()
    order = {a[i]:i + 1 for i in range(n)}
    cnt = set()
    ans = True
    for i in range(m):
        cnt.add(b[i])
        if len(cnt)  < order[b[i]]:
            ans = False
            break
    if ans:
        print("YA")
    else:
        print("TIDAK")
    

for _ in range(II()):
    solve()
