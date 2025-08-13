import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, tot = IL()
    tot *= 8
    a = IL()
    cnt = Counter(a)
    val = tot / len(cnt)
    # print(val)
    val  = int(val)
    a = sorted(list(set(a)))
    vals = []
    for K in range(1, n + 1):
        val = math.ceil(math.log2(K)) * n
        if val <= tot:
            vals.append(K)
    # print(vals)
    val = max(vals)
    # print(a)
    # print(val, len(cnt))
    k = len(cnt) - val
    if k <= 0:
        print(0)
        return
    
    left = 0
    cur = 0
    ans = float('inf')
    aa = a * 2
    edges = [0, len(a) - 1, len(a), len(aa) - 1]
    # print(aa, k)

    # print('k,',k)
    for right in range(len(aa)):
        cur += cnt[aa[right]]
        if right >= k - 1:
            for edge in edges:
                if left <= edge <= right:
                    # print(left, right, cur)
                    ans = min(ans, cur)
            cur -= cnt[aa[left]]
            left += 1
    print(ans)

    

solve()
