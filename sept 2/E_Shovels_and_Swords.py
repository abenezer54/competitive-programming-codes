import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    a, b = IL()
    mx = max(a, b)
    mn = min(a, b)
    if mx >= 2 * mn:
        print(mn)
    else:
        diff = mx - mn
        ans = min(ceil(diff / 2), mn)
        # print('prev, ans)
        mn -= ans
        mx -= 2 * ans
        ans += min(mn, (mn + mx) // 3)
        print(ans)


for _ in range(II()):
    solve()
