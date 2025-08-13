import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, q = IL()
    arr = [0]
    # print(q)
    cnt = [0]
    for _ in range(n):
        cmd, val = IL()
        if cmd == 1:
            arr.append(val)
            cnt.append(cnt[-1]+1)
        else:
            if cnt[-1] > int(1e18):
                continue
            cnt[-1] *= (val+1) 

    # print(cnt)
    def find_ans(k):
        idx = bisect_left(cnt, k)
        m = cnt[idx - 1] + 1

        if m == 0 or k % m == 0:
            return arr[idx]
        while m != 0 and k % m != 0:
            k %= m
            idx = bisect_left(cnt, k)
            m = cnt[idx - 1] + 1
        return arr[idx]
        
 
    queries = IL()
    ans = []
    for query in queries:
        # print(query)
        ans.append(find_ans(query))
    print(*ans)

for _ in range(II()):
    solve()
