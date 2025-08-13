import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    p = IL()
    a = IL()
    ind = [0] * (n + 1)
    for node in p:
        ind[node] += 1
    leaf = [0] * (n + 1)
    start = []
    for node in range(1, n + 1):
        if ind[node] == 0:
            leaf[node] = 1
            start.append(node)
    


    def check(mid):
        cur = ind[:]
        stack = start[:]
        val = a[:]
        while stack:
            node = stack.pop()
            parent = -1 if node == 1 else p[node - 2]
            if leaf[node] == 1:
                if val[node - 1] > mid:
                    return False
                else:
                    if parent != -1:
                        val[parent - 1] -= (mid - val[node - 1] )
            else:
                if val[node - 1] > 0:
                    return False
                if parent != -1:
                    val[parent - 1] += val[node - 1]

            if parent != -1:
                cur[parent] -= 1
                if cur[parent] == 0:
                    stack.append(parent)
        return True
    # print(check(2))
    l, r = 0, int(1e18)
    while l + 1 < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid
    print(r)





    

solve()
