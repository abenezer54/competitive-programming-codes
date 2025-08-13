import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    s = S()
    u = 0
    for char in s:
        if char.isupper():
            u += 1
    # print(u)
    if u * 2 > len(s):
        print(s.upper())
    else:
        print(s.lower())


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()

# Disjoint Set Union (DSU) / Union-Find
parent = list(range())  # Initialize parent array
size = [1 for _ in range()]  # Initialize size array

def find(node):
    """Find the root of x with path compression"""
    root = node
    while root != parent[root]:
        root = parent[root]
    
    while node != root:
        nxt = parent[node]
        parent[node] = root  # Path compression
        node = nxt
    return root

def union(x, y):
    """Union by size: attach smaller tree to the larger one"""
    rootx = find(x)
    rooty = find(y)
    if rootx != rooty:
        if size[rootx] > size[rooty]:
            rootx, rooty = rooty, rootx  # Ensure rooty is the larger root
        parent[rootx] = rooty  # Merge trees
        size[rooty] += size[rootx]  # Update the size of rooty
