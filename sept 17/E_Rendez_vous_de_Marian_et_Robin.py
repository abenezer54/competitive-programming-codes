import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m, h = IL()
    horse = set(sorted(IL()))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        i, j, w = IL()
        adj[i].append((j, w))
        adj[j].append((i, w))

    def dijkstra(x):
        heap =[(0, x, 0)]
        mn = defaultdict(lambda: float('inf'))
        while heap:
            w, node, have_horse = heapq.heappop(heap)
            if node in horse:
                have_horse = 1
            if (node, have_horse) in mn:
                continue
            
            mn[(node, have_horse)] = w

            for nei, wi in adj[node]:
                if (nei, have_horse) not in mn:
                    if have_horse:
                        heapq.heappush(heap, (wi//2 + w, nei, have_horse))
                    else:
                        heapq.heappush(heap, (w + wi, nei, have_horse))
        return mn
    
    fshort = dijkstra(1)
    sshort = dijkstra(n)
    ans = float('inf')
    for node in range(1, n + 1):
        mx1 = min(fshort[(node, 0)], fshort[(node, 1)])
        mx2 = min(sshort[(node, 0)], sshort[(node, 1)])
        mx = max(mx1, mx2)
        ans = min(ans, mx)

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
    

for _ in range(II()):
    solve()
