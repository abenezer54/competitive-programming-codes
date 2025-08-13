import sys
import math, heapq, random
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

    cnt1 = Counter(s)
    cnt2 = Counter(t)
    if cnt1 != cnt2:
        print("NO")
        return
    if n == 4:
        if s[1] == t[1] and s[2] == t[2]:
            print("YES")
        else:
            print("NO")
        return

    if n == 5:
        if s[2] == t[2]:
            print("YES")
        else:
            print("NO")
        return
    print("YES")
    

for _ in range(II()):
    solve()
