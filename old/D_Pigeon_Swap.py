import sys
from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
from math import gcd, lcm, ceil, sqrt
from bisect import bisect_left, bisect_right


I = lambda: sys.stdin.readline().strip()
II = lambda: int(I())
LII = lambda: list(map(int, I().split()))


class Node:
    def __init__(self, val):
        self.val = val


def solve():
    n, q = LII()
    mp = {i: i for i in range(n)}

    parent = [mp[i] for i in range(n)]

    for _ in range(q):
        a, *b = LII()
        if a == 3:
            b = b[0]
            print(parent[b - 1]+ 1)

        else:
            b, c = b

            if a == 1:
                parent[b - 1] = mp[c - 1]
            else:
                mp[c - 1], mp[b - 1] = mp[b - 1], mp[c - 1]


# t = int(input())
t = 1

for _ in range(t):
    solve()
