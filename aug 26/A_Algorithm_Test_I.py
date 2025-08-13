import sys
import math
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    m = II()
    a = IL()
    cnt = Counter(a)
    print(math.perm(len(cnt)))
    # print(math.perm(3))
solve()
