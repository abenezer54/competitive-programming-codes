import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    a = IL()
    b = IL()
    rand = random.randint(1000, 10000000)
    vals = set()
    for i in range(n):
        vals.add(a[i] ^ rand)
        vals.add(b[i] ^ rand)

    arr = [(a[i], b[i]) for i in range(n)]
    arr.sort(key=lambda x: (x[1], x[0]))
    # arr.sort()
    print(arr)
    ans = 0
    for x in vals:
        num = x ^ rand
        if arr[-1][1] < num:
            continue
        l, r = -1, n - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if arr[mid][1] >= num:
                r = mid
            else:
                l = mid
        can_buy_start = r
        if num == 2:
            print('hsdks', can_buy_start)
        
        if arr[can_buy_start][0] >= num:
            ans = max(ans, num * (n - r))
        else:
            l, r = can_buy_start, n
            while l + 1 < r:
                mid = (l + r) // 2
                if arr[mid][0] < num:
                    l = mid
                else:
                    r = mid
            if num == 2:
                print('bottom', l)
            if not(l - can_buy_start + 1 > k):         
                ans = max(ans, num * (n - can_buy_start))
        print('here', num, ans)

    print(ans)




tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()