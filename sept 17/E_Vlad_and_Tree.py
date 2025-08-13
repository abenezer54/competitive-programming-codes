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
        self.parent = list(range(size))
        self.size = [1 for _ in range(size)]
 
    def find(self, x):
        rt = x
        while rt != self.parent[rt]:
            rt = self.parent[rt]
        while x != rt:            
            nxt = self.parent[x]
            self.parent[x] = rt
            x = nxt
        return rt
 
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:            
            if self.size[px] > self.size[py]:
                px, py = py, px
            self.parent[px] = py
            self.size[py] += self.size[px]
 
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
def solve():
    n, m = IL()
    edges = [IL() + [1] for _ in range(m)]
    ava = set()
    tot = 0
    for bit in range(32, -1, -1):
        dsu = Dsu(n + 10)
        for x, y, w, valid in edges:
            tot |= w
            if (1 << bit) & w:
                continue
            elif valid:
                dsu.union(x, y)

        root = dsu.find(1)
        if dsu.size[root] == n:
            ava.add(bit)
            for i in range(len(edges)):
                if ((1 << bit) & edges[i][2]) and edges[i][-1] :
                    edges[i][-1] = 0
    for bit in range(32):
        if bit in ava and tot & (1 << bit):
            tot -= (1 << bit)
    print(tot)


    



    

   

for _ in range(II()):
    S()
    solve()
