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
            if rootx > rooty:
                rootx, rooty = rooty, rootx  # Ensure rooty is the larger root
            self.parent[rootx] = rooty  # Merge the trees
            self.size[rooty] += self.size[rootx]  # Update the size of the root rooty

    def is_connected(self, x, y):
        # Check if x and y are in the same set
        return self.find(x) == self.find(y)
def solve():
    n, q = IL()
    dsu = Dsu(n + 1)
    for _ in range(q):
        op = IL()
        if op[0] == 1:
            x = op[1]
            c = op[2]
            if x + 1 <= n and dsu.find(x) != dsu.find(x + 1):
                dsu.union(x, x + 1)
            if x - 1 >= 1 and dsu.find(x) != dsu.find(x - 1):
                dsu.union(x, x - 1)
            dsu.union(x, c)
            if x + 1 <= n and dsu.find(x) != dsu.find(x + 1):
                dsu.union(x, x + 1)
            if x - 1 >= 1 and dsu.find(x) != dsu.find(x - 1):
                dsu.union(x, x - 1)
            # print(dsu.parent, dsu.size)
        else:
            root = dsu.find(op[1])
            print(dsu.size[root])
    


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()