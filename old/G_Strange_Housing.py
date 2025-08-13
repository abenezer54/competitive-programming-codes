import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
# Disjoint Set Union (DSU) / Union-Find Class
class Dsu:
    def __init__(self, size):
        # Initialize the parent and size arrays
        self.parent = list(range(size))  # Each element is its own parent initially
        self.size = [1 for _ in range(size)]  # Initial size of each set is 1

    def find(self, node):
        # Find the root of x with path compression
        root = node
        while root != self.parent[root]:
            root = self.parent[root]  # Move up to the parent
        while node != root:
            nxt = self.parent[node]
            self.parent[node] = root  # Path compression step
            node = nxt
        return root

    def union(self, x, y):
        # Union by size: attach smaller tree to the larger tree
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.size[rootx] > self.size[rooty]:
                rootx, rooty = rooty, rootx  # Ensure rooty is the larger root
            self.parent[rootx] = rooty  # Merge the trees
            self.size[rooty] += self.size[rootx]  # Update the size of the root rooty

    def cnt_components(self):
        cnt = 0
        for i in range(1, len(self.parent)):
            if i == self.find(i):
                cnt += 1
        return cnt

    def is_connected(self, x, y):
        # Check if x and y are in the same set
        return self.find(x) == self.find(y)

def solve():
    n, m = IL()
    adj = [[] for _ in range(n + 1)]
    dsu = Dsu(n + 1)
    for _ in range(m):
        u, v = IL()
        dsu.union(u, v)
        adj[u].append(v)
        adj[v].append(u)
    components = dsu.cnt_components()
    if components != 1:
        print("NO")
        return

    ans = []
    vis = [0] * (n + 1)
    vis[1] = 1
    stack = [(1, 0)]
    while stack:
        node, x = stack.pop()
        if x % 2 == 0:
            ans.append(node)
        
        for nei in adj[node]:
            if vis[nei] == 0:
                stack.append((nei, x + 1))
                vis[nei] = 1
    print("YES")
    print(len(ans))
    print(*ans)







tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()