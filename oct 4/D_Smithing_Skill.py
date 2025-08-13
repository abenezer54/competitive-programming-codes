import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    a = IL()
    b = IL()
    c = IL()
    mp = defaultdict(lambda: float('inf'))
    for i in range(n):
        cost = a[i] - b[i]
        mp[cost] = min(mp[cost], a[i])
    temp = [(key, val) for key, val in mp.items()]
    temp.sort()
    mn = temp[0][1]
    arr = [temp[0]]
    for i in range(1, len(temp)):
        if temp[i][1] < mn:
            arr.append(temp[i])
            mn = temp[i][1]

    mx = arr[0][1]
    dp = [0] * (mx + 1)
    arr.sort(key=lambda x: x[1])
    dp[arr[0][1]] = 1
    idx = 0
    for i in range(arr[0][1] + 1, len(dp)):
        if idx < len(arr) - 1 and arr[idx + 1][1] <= i:
            idx += 1
        cost = arr[idx][0]
        dp[i] = 1 +  dp[i - cost]

    ans = 0
    for i in range(m):
        if c[i] > mx:
            diff = c[i] - mx
            val = math.ceil(diff / temp[0][0])
            ans += val
            ans += dp[c[i] - (val * temp[0][0])]
        else:
            ans += dp[c[i]]
    print(ans * 2)

solve()
