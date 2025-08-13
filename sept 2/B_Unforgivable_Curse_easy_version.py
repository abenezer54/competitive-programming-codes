import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    s = S()
    t = S()
    if n <= 3:
        if s == t:
            print("YES")
        else:
            print("NO")
        return
    cs = Counter(s)
    ct = Counter(t)
    if n == 4:
        if cs == ct and s[2] == t[2] and s[1] == t[1]:
            print("YES")
        else:
            print("NO")
        return

    if n == 5:
        if cs == ct and s[2] == t[2]:
            print("YES")
        else:
            print("NO")
    
        return
    if cs == ct:
        print('YES')
    else:
        print("NO")

for _ in range(II()):
    solve()
