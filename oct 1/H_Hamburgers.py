import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    s = S()
    cnt = Counter(s)
    a = IL()
    b = IL()
    money = II()
   
    def check(mid):
        need = [cnt["B"] * mid, cnt["S"] * mid, cnt["C"] * mid]
        cur = money
        for i in range(3):
            if a[i] < need[i]:
                val = need[i] - a[i]
                cur -= val * b[i]
        return cur >= 0

    l, r = 0, int(1e18)
    while l + 1 < r:
        mid = (l + r) // 2
        if check(mid):
            l = mid
        else:
            r = mid
    print(l)

solve()
