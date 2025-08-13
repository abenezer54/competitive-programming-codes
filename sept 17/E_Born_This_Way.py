import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m, ta, tb, k = IL()
    a = IL()
    b = IL()
    a = [num + ta for num in a]
    # print(a)
    # print(b)

    j = 0
    i = 0
    tot = 0
    while i < m and j < n and k:
        idx = bisect_right(a, b[i]) - 1
        
        if idx < j:
            i += 1
        else:
            # print(i, j)
            ifa = m - i
            ifb = idx - j + 1
            # print('here', i, idx, j, ifa, ifb)
            if ifa > ifb:
                j = idx + 1
                k -= ifb
                i += 1
            else:
                i += 1
                k -= 1
            # print('bot', i,j)
        if k == 0:
            while i < m:
                idx = bisect_right(a, b[i]) - 1
        
                if idx < j:
                    i += 1
                else:
                    break
            if i == m:
                print(-1)
            else:
                print(b[i] + tb)
            return
    print(-1)
        


solve()
