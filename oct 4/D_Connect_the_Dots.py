import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
# Disjoint Set Union (DSU) / Union-Find Class
class Dsu:
    def __init__(self, size):
        # Initialize the parent and size arrays
        self.parent = list(range(size))  # Each element is its own parent initially

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
                self.parent[rooty] = rootx
            else:
                self.parent[rootx] = rooty

    def is_connected(self, x, y):
        # Check if x and y are in the same set
        return self.find(x) == self.find(y)
        
    def count_components(self):
        cnt = 0
        for node in range(1, len(self.parent)):
            if node == self.find(node):
                cnt += 1
        return cnt
    
def solve():
    n, m = IL()
    edges = [[] for _ in range(11)]
    for _ in range(m):
        a, d, k = IL()
        edges[d].append((a, a + (k * d)))
    
    graphs = [Dsu(n + 1) for _ in range(11)]
    for d in range(1, 11):
        for u, v in edges[d]:
            while graphs[d].find(u) + d <= v:
                graphs[d].union(u, graphs[d].find(u) + d)

    for node in range(1, n + 1):
        for d in range(2, 11):
            graphs[1].union(node, graphs[d].find(node))
    print(graphs[1].count_components())
    

for _ in range(II()):
    solve()
