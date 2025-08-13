import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    a = IL()
    b = IL()
    cnt = 0
    def check(mid):
        cnt = 0           
        for x, y in zip(a, b):
            val = max(0, ((x - mid) // y) + 1)
            cnt += val
        return cnt
    
    def calc_ans(mn):
        tot = 0
        for x, y in zip(a, b):
            val = max(0, ((x - mn) // y) + 1)
            sm = (val * ((2 * x) + ((val - 1) * -y))) // 2
            tot += sm
        return tot
    
    l, r = 0, int(1e18)
    cnt = 0
    while l + 1 < r:
        mid = (l + r) // 2
        val = check(mid)
        if val >= k:
            cnt = val
            l = mid
        else:
            r = mid
    
    if cnt != k:
        l += 1
    ans = calc_ans(l)
    off = k - check(l)
    ans += off * (l - 1)
    print(ans)
for _ in range(II()):
    solve()
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