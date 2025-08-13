import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, m, k = IL()
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = IL()
        adj[x].append(y)
        adj[y].append(x)

    mp = defaultdict(int)
    col = [0] * (n + 1)
    start = end = -1

    for v in range(1, n + 1):
        if col[v] == 0:
            found = False
            cur = 1
            stack = [v]
            hold = []
            while stack and not found:
                node = stack[-1]
                col[node] = cur
                mp[col[node]] = node
                cur += 1
                for nei in adj[node]:
                    if col[nei] not in [0, -1] and col[node] - col[nei] + 1 > k:
                        found = True
                        start = col[nei]
                        end = col[node]
                    if col[nei] == 0:
                        stack.append(nei)
                if node == stack[-1]:
                    hold.append(stack.pop())
                    cur -= 1
            if found:
                break
            while hold:
                col[hold.pop()] = -1
                
    ans = []
    for i in range(start, end + 1):
        ans.append(mp[i])
    print(len(ans))
    print(*ans)
 
solve()
