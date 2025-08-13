import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    s = S()
    c = Counter(s)
    if len(c) == 1:
        print(0)
        return
    cnt = ans = 0
    flag = False
    if s[-1] == '1':
        flag = True
    for i in range(n - 1, -1, -1):
        if flag and s[i] == '1':
            cnt += 1
            ans += 2 if cnt != 1 else 1
            if i == n - 1:
                ans -= 1
            flag = False

        if s[i] == '0':
            flag = True
    print(ans)

for _ in range(II()):
    solve()
