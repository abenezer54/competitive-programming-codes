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

    def is_connected(self, x, y):
        # Check if x and y are in the same set
        return self.find(x) == self.find(y)
def solve():
    n, m = IL()
    g = Dsu(n)
    ans = 0
    for _ in range(m):
        u, v = IL()
        u -= 1
        v -= 1
        if g.is_connected(u, v):
            ans += 1
        else:
            g.union(u, v)
    print(ans)


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()