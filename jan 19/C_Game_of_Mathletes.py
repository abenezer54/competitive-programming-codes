import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    a = IL()
    cnt = Counter()
    rand = random.randint(1000, 1000000)
    for val in a:
        cnt[rand ^ val] += 1
    x = y = 0
    temp = [(key, val) for key, val  in cnt.items()]
    
    for key, val in temp:
        if k - (rand ^ key) == (rand ^ key):
            x += cnt[key] // 2
            y += cnt[key] & 1
            continue
        z = min(cnt[key], cnt[rand ^ (k - (rand ^ key))])
        x += z
        # print(key ^ rand, z)
        cnt[key] -= z
        cnt[rand ^ (k - (rand ^ key))] -= z
        y += max(0, cnt[key])
        y += max(0, cnt[rand ^ (k - (rand ^ key))])
    print(x)




tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()