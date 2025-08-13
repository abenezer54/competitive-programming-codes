import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def MUX(arr, n):
    found = False
    for i in range(n):
        if arr[i] == 0:
            found = True
    if not found:
        return 0
    
    for i in range(n):
        if arr[i] == 0:
            found = True
        while (arr[i] >= 1 and arr[i] <= n and arr[i] != arr[arr[i] - 1]):
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp

    for i in range(n):
        if (arr[i] != i + 1):
            return i + 1

    return n + 1

def solve():
    n, m = IL()
    maxx = 0
    for _ in range(n):
        a = IL()
        
        mux1 = MUX(a[1:], len(a) - 1)
        a.append(mux1)
        mux2 = MUX(a[1:], len(a) - 1)
        maxx = max(maxx, mux1, mux2)
        # print('mux1', mux1, mux2)
    # print(n, m, maxx)
    if maxx >= m:
        print(maxx * (m + 1))
        # print('up')
    else:
        val1 = maxx * (maxx + 1)
        
        x = (m * (m + 1)) // 2
        y = (maxx * (maxx + 1)) // 2
        z = x - y
        # print('val1', val1)
        print(val1 + z)

    

for _ in range(II()):
    solve()
