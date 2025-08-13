import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
from types import GeneratorType

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def solve():
    n = IL()[0]
    adj = [[] for _ in range(n + 1)]
    ind = [0] * (n + 1)
    a = [0] + IL()
    if n == 1:
        print(a[1])
        return

    for _ in range(n - 1):
        x, y = IL()
        adj[x].append(y)
        adj[y].append(x)
        ind[x] += 1
        ind[y] += 1
    dp1 = [0] * (n + 5)
    dp2 = [0] * (n + 5)

    vis = [0] * (n + 1)

    @bootstrap
    def dfs(node):
        dp1[node] += a[node]

        for nei in adj[node]:
            if vis[nei] == 0:
                vis[nei] = 1
                yield dfs(nei)
                dp1[node] += dp2[nei]
                dp2[node] += max(dp1[nei], dp2[nei])
        yield None

    vis[1] = 1
    dfs(1)

    print(sum(a) * 2 - (max(dp1 + dp2)))
                




tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()