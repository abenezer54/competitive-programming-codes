import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    p = IL()
    if n == 7:
        print(p)
    ind = [0] * (n + 1)
    for i in range(len(p)):
        ind[p[i]] += 1
    mp = [[] for _ in range(n + 1)]
    que = deque()
    for v in range(1, n + 1):
        if ind[v] == 0:
            que.append(v)
            # mp[v].append(1)
    adj = [[] for _ in range(n + 1)]

    while que:
        node  = que.popleft()
        sm = 0
        for val in mp[node]:
            sm += val[0]
        mp[p[node - 2]].append([sm + 1, node])
        adj[p[node - 2]].append(node)
        ind[p[node - 2]] -= 1
        if ind[p[node - 2]] == 0:
            que.append(p[node - 2])
    r = sorted(mp[0][0])
    que = deque([(1, r)])
    vis = set([1])
    ans = 0
    while que:
        node, r = que.popleft()
        arr = sorted(mp[node], reverse=True)
        prev = arr[0]
        left, right = 0, len(arr) - 1
        while left < right:
            mn = min(arr[left][0], arr[right][0])
            ans += mn
            arr[left][0] -= mn
            arr[right][0] -= mn
            if arr[left][0] == 0:
                left += 1
            if arr[right][0] == 0:
                right -= 1
        if n == 7:
            print(node, arr, left)
        if arr[left][0] > 1 and arr[left][0] not in vis:
            que.append((arr[left][1], arr[left][0]))
            vis.add(arr[left][0])
    print(ans)

    
    

for _ in range(II()):
    solve()
