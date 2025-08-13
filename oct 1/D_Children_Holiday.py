import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    m, n = IL()
    a = [IL() for _ in range(n)]
    def check(mid):
        tot = 0
        for t, z, y in a:
            cur = mid
            one_cycle = t * z + y
            val = cur // one_cycle
            tot += val * z
            cur = cur % one_cycle
            cur = min(cur, t * z)
            tot += cur // t
        return tot >= m
    
    def find_ans(mid):
        arr = []

        for t, z, y in a:
            mmd = mid
            one_cycle = t * z + y
            val = mmd // one_cycle
            cur = val * z
            mmd = mmd % one_cycle
            mmd = min(mmd, t * z)
            cur += mmd // t
            arr.append(cur)
        return arr

    
    l, r = -1, int(1e18)
    while l + 1 < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid
    print(r)
    ans = find_ans(r)
    tot = sum(ans)
    for i in range(len(ans)):
        if tot > m:
            diff = tot - m
            mn = min(diff, ans[i])
            tot -= mn
            ans[i] -= mn
        else: 
            break
    
    print(*ans)
solve()
