import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def find_divisors(number):
    divisors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    return divisors
def solve():
    l, r, x, y, k = IL()
    arr = list(range(x, y + 1))
    # print(arr)
    for a in range(l, r + 1):
        if a >= k and a % k == 0 and x <= a//k <= y:
            print("YES")
            return

    print("NO")
                


solve()
