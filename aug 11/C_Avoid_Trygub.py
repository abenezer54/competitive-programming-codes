import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    s = list(S())
    order = 'bugyrt'
    ans = []
    r = []
    for ch in s:
        if ch in order:
            ans.append(ch)
        else:
            r.append(ch)
    ans.sort(key=lambda x: order.index(x))
    # print(ans)
    print(''.join(ans + r))

    

for _ in range(II()):
    solve()
