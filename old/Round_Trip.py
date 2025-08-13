import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m = IL()
    adj = [[] for _ in range(n + 1)]
    for _  in range(m):
        a, b = IL()
        adj[a].append(b)
        adj[b].append(a)

    col = [0] * (n + 1) 
    parent = [-1] * (n + 1)
    for start in range(1, n + 1):
        if col[start] == 0:
            # print(start)
            stack = [(start, 1)]
            col[start] = 1
            while stack:
                node, level = stack.pop()
                for nei in adj[node]:
                    if col[nei] == 0:
                        stack.append((nei, level + 1))
                        col[nei] = level + 1
                        parent[nei] = node
                        break
                    else:
                        if level - col[nei] >= 2:
                            # print('here')
                            path = [node]
                            cur = node
                            while parent[cur] != -1:
                                path.append(parent[cur])
                                cur = parent[cur]
                            print(len(path) + 1)
                            print(*path[::-1], path[-1])
                            return
    print('IMPOSSIBLE')





tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()