import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m, k = IL()
    a = sorted(list(S()))
    b = sorted(list(S()))
    i = j = 0
    last = -1
    cnt = 0
    ans = []
    while i < n and j < m:
        if cnt == k:
            if last == 0:
                ans.append(b[j])
                j += 1
                cnt = 1
                last = 1
            else:
                ans.append(a[i])
                i += 1
                cnt = 1
                last = 0
            continue
        
        if a[i] <= b[j]:
            ans.append(a[i])
            i += 1
            if last == 0:
                cnt += 1
            else:
                cnt = 1
            last = 0
        else:
            ans.append(b[j])
            j += 1
            if last == 1:
                cnt += 1
            else:
                cnt = 1
            last = 1
    print("".join(ans))



for _ in range(II()):
    solve()
