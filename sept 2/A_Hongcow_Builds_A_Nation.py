import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m, k = IL()
    c = set(IL())
    adj = defaultdict(list)
    for i in range(m):
        x, y = IL()
        adj[x].append(y)
        adj[y].append(x)
    vis = [0] * (n + 1)
    mx = 0
    arr = []
    ans = 0
    for v in range(1, n + 1):
        if vis[v] == 0:
            stack = [v]
            vis[v] = 1
            isgov = False
            cnt = 0
            edges = 0
            while stack:
                cnt += 1
                node = stack.pop()
                edges += len(adj[node])
                if node in c:
                    isgov = True
                
                for nei in adj[node]:
                    if vis[nei] == 0:
                        stack.append(nei)
                        vis[nei] = 1
            mx_edge = (cnt * (cnt - 1)) // 2
            ans += mx_edge - (edges // 2)
            if isgov:
                mx = max(mx, cnt)
            else:
                arr.append(cnt)
            
    for num in arr:
        ans += mx * num
        mx += num
    print(ans)
        
solve()
