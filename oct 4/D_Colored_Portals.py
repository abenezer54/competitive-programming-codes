import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def left_search(target, arr):
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        if arr[mid] <= target:
            l = mid
        else:
            r = mid
    return arr[l]
    

def right_search(target, arr):
    l, r = -1, len(arr) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if arr[mid] >= target:
            r = mid
        else:
            l = mid
    return arr[r]


def share_point(a, b):
        for val in a:
            if val in b:
                return True
        return False
    

def solve():
    n, q = IL()
    s = [0] + S().split()
    pairs = ["BG", "BR", "BY", "GR", "GY", "RY"]
    arr = defaultdict(list)
    for node in range(1, n + 1):
        arr[s[node]].append(node)

    for key in arr:
        arr[key].sort()
 
    def find_ans(node1, node2):
        cur = s[node1]
        target = (node1 + node2) / 2
        cost = float('inf')
        for pair in pairs:
            if pair != cur and pair != s[node2] and arr[pair]:
                left = left_search(target, arr[pair])
                if node1 <= left <= node2:
                    cost = 0
                else:
                    cost = min(cost, abs(node1 - left) * 2)
                right = right_search(target, arr[pair])
                if node1 <= right <= node2:
                    cost = 0
                else:
                    cost = min(cost, abs(node2 - right) * 2)
        return abs(node1 - node2) + cost

   
    for _ in range(q):
        a, b = IL()
        if share_point(s[a], s[b]):
            print(abs(a - b))
        else:
            a, b = sorted([a, b])
            ans = find_ans(a, b)
            if ans == float('inf'):
                print(-1)
            else:
                print(ans)
        
    

for _ in range(II()):
    solve()
