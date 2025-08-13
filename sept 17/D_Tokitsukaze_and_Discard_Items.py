import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
   n, m, k = IL()
   a = IL()
   ans = 0
   heap = []
   vals = 0
   ans = set()
   col = 0
   for i in range(m):
      cur = (a[i] - 1 -vals)//k
   
      while heap and heap[0] - 1 //k < cur:
         ans.add(col)
         heapq.heappop(heap)
         vals += 1
      cur = (a[i] - 1 -vals)//k
      heapq.heappush(heap, cur)
      col += 1
   # print(ans)
   if heap:

      ans.add(col)
   print(len(ans))
solve()
