import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def fp(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(int(n))
    return primfac


def solve():
    n = II()
    a = IL()
    start, dest = IL()
    divisors = defaultdict(list)
    for i in range(n):
        x = fp(a[i])
        for j in range(len(x)):
            divisors[x[j]].append(i + 1)
    # print(divisors)
    adj = [[] for _ in range(n + 1)]
    for arr in divisors.values():
        for i in range(len(arr) - 1):
            if arr[i] != arr[i + 1]:
                adj[arr[i]].append(arr[i + 1])
                adj[arr[i + 1]].append(arr[i])
    # print(adj)
    heap = [(0, start)]
    vis = [0] * (n + 1)
    vis[start] = 1
    ans = float('inf')
    par = [-1] * (n + 1)

    while heap:
        w, node = heapq.heappop(heap)

        if node == dest:
            ans = min(ans, w)
            break
        for nei in adj[node]:
            if vis[nei] == 0:
                heapq.heappush(heap, (w + 1, nei))
                par[nei] = node
                vis[nei] = 1

    if ans == float('inf'):
        print(-1)
        return
    path = [dest]
    cur = dest
    # print(par)
    while par[cur] != start and par[cur] != -1:
        path.append(par[cur])
        cur = par[cur]
    if len(path) <  ans + 1:
        path.append(start)
    print(len(path))
    print(*path[::-1])

solve()
