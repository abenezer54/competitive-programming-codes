import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    k, l1, r1, l2, r2 = IL()
    p = 0
    def check(val, pp):
        return l2 <= val * pp <= r2

    def check_first(val, pp):
        if val * pp < l2:
            return 0
        if val * pp > r2:
            return 2
        return 1
    
    ans = 0
    cnt = 0
    while True: 
        power = pow(k, p)
        cnt += 1
        if cnt == 33:
            break
        start = -1
        l, r = l1 - 1, r1 + 1
        while l + 1 < r:
            mid = (l + r) // 2
            val = check_first(mid, power)
            if val == 1:
                start = mid
                break
            elif val == 0:
                l = mid
            else:
                r = mid

        if start == l1 - 1 and not check(start + 1, power):
            p += 1
            continue

        if start == -1 or start > r1:
            p += 1
            continue


        l, r = l1 - 1, start
        while l + 1 < r:
            mid = (l + r) // 2
            if check(mid, power):
                r = mid
            else:
                l = mid

        left_most = r

        l, r = left_most, r1 + 1
        while l + 1 < r:
            mid = (l + r) // 2
            if check(mid, power):
                l = mid
            else:
                r = mid
        right_most = l
           
        ans += right_most - left_most + 1


        p += 1
    print(ans)


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()