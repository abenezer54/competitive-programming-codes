import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    adj = [[] for _ in range(n + 1)]
    ind = [0] * (n + 1)
    for _ in range(n - 1):
        x, y = IL()
        adj[x].append(y)
        adj[y].append(x)
        ind[x] += 1
        ind[y] += 1

    mp = defaultdict(list)
    que = deque()
    for node in range(1, n + 1):
        if ind[node] == 1:
            que.append(node)
            mp[node].append([0, node])

    wait = []   
    x = []
    while que:
        node = que.popleft()
        arr = mp[node]
        arr.sort(reverse=True)
        if len(arr) >= 2:
            x.append((node,( arr[0], arr[1])))
        for i in range(1, len(arr)):
            wait.append(arr[i])

        
        for nei in adj[node]:
            ind[nei] -= 1
            #neibors best append
            mp[nei].append([arr[0][0] + 1, arr[0][1]])
            if ind[nei] == 1:
                que.append(nei)
    wait.sort(reverse=True)

    ans = 0
    vertices = [-1, -1, -1]
    # print(x)
    for node, vals in x:
        check = set([vals[0][1], vals[1][1]])
        cur = vals[0][0] + vals[1][0]
        if cur > ans:
            vertices = list(check) + [node]
            ans = cur

        for val, nei in wait:
            if nei not in check and nei != node:
                cur = vals[0][0] + vals[1][0] + val
                if cur > ans:
                    vertices = list(check) + [nei]
                    ans = cur
                    break
                else:
                    break
    print(ans)
    print(*vertices)
                    
tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()