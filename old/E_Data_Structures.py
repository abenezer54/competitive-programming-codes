import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()


class SegmentTree:


    def __init__(self, arr, zero_value):
        self.zero_value = zero_value 
        self.shift = 1 << (len(arr) - 1).bit_length()
        self.tree = [self.zero_value] * (self.shift << 1)
        self.build(arr)
        # print(self.tree)


    def build(self,arr):
        for i in range(len(arr)):
            self.tree[i + self.shift] = arr[i]
        
        for i in range(self.shift - 1, 0, -1):
            left_child = i << 1
            right_child = i << 1 | 1
            self.tree[i] = self.merge(self.tree[left_child], self.tree[right_child])
    

    def update(self, idx, val):

        tree_idx = idx + self.shift
        self.tree[tree_idx] = val
        node = tree_idx >> 1
        while node > 0:
            left_child = node << 1 
            right_child = node << 1 | 1
            self.tree[node] = self.merge(self.tree[left_child], self.tree[right_child])
            node >>= 1 
    

    def query(self, left, right):
        left += self.shift
        right += self.shift + 1
        ans = self.zero_value
        while left < right:
            if left & 1:
                ans = self.merge(ans, self.tree[left])
                left += 1
            
            if right & 1:
                right -= 1
                ans = self.merge(ans, self.tree[right])
            left >>= 1
            right >>= 1
        return ans

    def merge(self, node1, node2):
        return min(node1,  node2)
    



def solve():
    n, m = IL()
    a = [0] + IL()
    b = [0] + IL()
    for _ in range(m):
        query = IL()
        if len(query) == 4:



tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()