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
    prefix = [0] * n
    prev = 1
    prefix[0] = 1 if s[0] == "L" else 0
    for i in range(1, n):
        if s[i] == "L":
            if s[i - 1] == "R":
                prefix[i] = 1 + prev
                prev += 1
            else:
                prefix[i] = 1
                prev = 1 #check
        else:
            if s[i - 1] == "R":
                prev = 1
            else:
                prev += 1

    prefix = [0] + prefix
    
    suffix = [0] * n
    prev = 1
    suffix[-1] = 1 if s[-1] == "R" else 0
    for i in range(n - 2, -1, -1):
        if s[i] == "R":
            if s[i + 1] == "L":
                suffix[i] = 1 + prev
                prev += 1
            else:
                suffix[i] = 1
                prev = 1

        else:
            if s[i + 1] == "L":
                prev = 1
            else:
                prev += 1
    suffix.append(0)
    # print(prefix, suffix)
    ans = [1 + prefix[i] + suffix[i] for i in range(n + 1)]

    print(*ans)

for _ in range(II()):
    solve()
