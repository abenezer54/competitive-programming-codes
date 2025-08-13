class Dsu:
    def __init__(self, size):
        self.parent = list(range(size))  
        self.size = [1 for _ in range(size)]  

    def find(self, node):
        root = node
        while root != self.parent[root]:
            root = self.parent[root]  
        while node != root:
            nxt = self.parent[node]
            self.parent[node] = root  
            node = nxt
        return root

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.size[rootx] > self.size[rooty]:
                rootx, rooty = rooty, rootx  
            self.parent[rootx] = rooty  
            self.size[rooty] += self.size[rootx] 

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    print(random.randint(1))
    n, m1, m2 = IL()
    edges = []
    for _ in range(m1):
        edges.append(IL())
    graph2 = Dsu(n + 1)

    for _ in range(m2):
        u, v = IL()
        graph2.union(u, v)
    ans = 0
    graph1 = Dsu(n + 1)
    for u, v in edges:
        if not graph2.is_connected(u, v):
            ans += 1
        else:
            graph1.union(u, v)

    cmp2 = 0
    cmp1 = 0
    for node in range(1, n + 1):
        if node == graph2.find(node):
            cmp2 += 1
        if node == graph1.find(node):
            cmp1 += 1
    
    ans += cmp1 - cmp2
    print(ans)



tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()