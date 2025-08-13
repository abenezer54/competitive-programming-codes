import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = IL()
    cnt = Counter()
    ran = random.randint(1000, 1000000000)
    for val in a:
        cnt[val ^ ran] += 1
    arr = []
    for key, val in cnt.items():
        while val >= 2:
            arr.append(key ^ ran)
            val -= 2
    if len(arr) < 4: 
        print("NO")
        return
    arr.sort()
    ans = [arr[0], arr[1], arr[0], arr[-1], arr[-2], arr[1], arr[-2], arr[-1]]
    print("YES")
    print(*ans)


        


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()