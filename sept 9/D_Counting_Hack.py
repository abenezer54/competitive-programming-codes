import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = IL()
    tot = Counter(a)
    cur = Counter()
    ans = 0
    for i in range(n):
        cur[a[i]] += 1
        if tot[a[i]] == cur[a[i]]:
            ans += len(cur)
    print(ans)
for _ in range(II()):
    solve()
