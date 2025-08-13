import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, d = IL()
    a = IL()
    ans = 2
    for i in range(n - 1):
        diff = a[i + 1] - a[i]
        if diff > d * 2:
            ans += 2
        elif diff == d * 2:
            ans += 1
    print(ans)


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()

parent = list(range()) 
size = [1 for _ in range()]  

def find(node):
    root = node
    while root != parent[root]:
        root = parent[root]
    
    while node != root:
        nxt = parent[node]
        parent[node] = root  # Path compression
        node = nxt
    return root

def union(x, y):
    rootx = find(x)
    rooty = find(y)
    if rootx != rooty:
        if size[rootx] > size[rooty]:
            rootx, rooty = rooty, rootx  
        parent[rootx] = rooty
        size[rooty] += size[rootx]  
