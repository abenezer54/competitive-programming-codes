import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = IL()
    cnt = Counter()
    rand = random.randint(1000, int(1e10))

    ss = []
    vis = set()
    for val in a:
        if val ^ rand not in vis:
            ss.append(val ^ rand)
            vis.add(val ^ rand)
    
    tot = len(ss)
    cur_cnt = 1
    ans = [-1] * n
    j = 0
    x = 0
    # if n == 4:
    #     print(cnt, tot)
    for i in range(n):
        if x == tot:
            x = 0
            cur_cnt += 1
        
        # if n == 4:
            # print(i, cur_cnt)

        if cnt[a[i] ^ rand] != cur_cnt:
            ans[i] = a[i]
            cnt[a[i] ^ rand] += 1
            x += 1
        else:
            while cnt[ss[j % tot]] == cur_cnt:
                j += 1
            ans[i] = ss[j % tot] ^ rand
            cnt[ss[j % tot]] += 1
            x += 1
    print(*ans)


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()