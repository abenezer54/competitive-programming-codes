import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    s = S()
    # print(n, s)
    cnt = [[0] * 26 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        idx = ord(s[i]) - 97
        for j in range(26):
            cnt[i][j] += cnt[i + 1][j]
            if j == idx:
                cnt[i][j] += 1
    # print(cnt)
    ans = 0
    for i in range(1, n):
        idx = ord(s[i]) - 97
        cur = cnt[i][idx]
        ans += cur
    print(ans)


for _ in range(II()):
    solve()
