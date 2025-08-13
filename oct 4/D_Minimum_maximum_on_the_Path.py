import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m, d = IL()
    adj = defaultdict(list)
    for _ in range(m):
        a, b, c = IL()
        adj[a].append((b, c))

    def check(mid):
        stack = [(1, 0, 0)]
        vis = [0] * (n + 1)
        ans = float('inf')
        found = False
        while stack:
            # print(stack)
            node, mx, depth = stack.pop()
            if node == n:
                ans = min(ans, mx)
                found = True
            
            if depth == d:
                continue
            
            for nei, w in adj[node]:
                if w <= mid and vis[nei] == 0:
                    stack.append((nei, max(w, mx), depth + 1))
                    vis[nei] = 1
        return found, ans
    

    # print(check(7))
    ans = float('inf')
    l, r = -1, int(1e9) + 10
    while l + 1 < r:
        mid = (l + r) // 2
        found, val = check(mid)
        if not found:
            l = mid
        else:
            r = mid
            ans = min(ans, val)

    if ans == float('inf'):
        print(-1)
        return

    def find_ans(val):
        stack = [(1, 0, 0)]
        parent = [-1] * (n + 1)
        vis = [0] * (n + 1)
        start = n
        while stack:
            # print(stack)
            node, mx, depth = stack.pop()
            if node == n:
                if mx == val:
                    break
            
            if depth == d:
                continue
            
            for nei, w in adj[node]:
                if w <= val and vis[nei] == 0:
                    parent[nei] = node
                    stack.append((nei, max(w, mx), depth + 1))
                    vis[nei] = 1
        path = [start]
        cur = start
        while parent[cur] != -1:
            path.append(parent[cur])
            cur = parent[cur]
        return path[::-1]
    
    arr = find_ans(ans)
    print(len(arr) - 1)
    print(*arr)

solve()
