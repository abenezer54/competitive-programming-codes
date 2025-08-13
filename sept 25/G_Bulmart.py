import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = IL()
        adj[x].append(y)
        adj[y].append(x)

    stores = [[] for _ in range(n + 1)]
    w = II()
    for _ in range(w):
        c, k, p = IL()
        stores[c].append([p, k])
    # for city in range(1, n + 1):
    #     stores[city].append([0, 0])
    #     stores[city].sort()
    #     for j in range(1, len(stores[city])):
    #         stores[city][j][1] += stores[city][j - 1][1]

    # print(stores)
    def check(mid, city, amount, budget):
        que = deque([city])
        k = 0
        heap = []
        vis = [0] * (n + 1)
        vis[city] = 1
        while que and k <= mid:

            ln = len(que)
            for _ in range(ln):
                node = que.popleft()
                # print('node', node, stores[node])
                for val in stores[node]:
                    # print('val',val)
                    heapq.heappush(heap, val)

                for nei in adj[node]:
                    if vis[nei] == 0:
                        vis[nei] = 1
                        que.append(nei)
            k += 1

        cur_budget = budget
        # print(heap)
        used = 0
        while heap and heap[0][1] * heap[0][0] <= cur_budget:
            price, val = heapq.heappop(heap)
            cur_budget -= price * val
            used += val 
        # print(used)
        if heap and cur_budget > 0:
            remain = cur_budget // heap[0][0]
            used += remain
        # print(used)
        if used >= amount:
            return True
        return False
                



    q = IL()[0]
    for query  in range(q):
        city, amount, budget = IL()
        l, r = 0, int(1e18)
        # if query == 0:
        #     print('by 2', check(2, city, amount, budget))
        while l + 1 < r:
            mid = (l + r) // 2
            if check(mid, city, amount, budget):
                r = mid
            else:
                l = mid
        if r == int(1e18):
            print(-1)
        else:
            print(r)


solve()
