import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    q = II()
    cost = defaultdict(int)
    for _ in range(q):
        cmd = IL()
        if len(cmd) == 4:
            r1, r2 = cmd[1], cmd[2]
            while r1 != r2:
                if r1 > r2:
                    cost[r1//2, r1] += cmd[-1]
                    cost[r1, r1//2] += cmd[-1]
                    r1 //= 2
                else:
                    cost[r2//2, r2] += cmd[-1]
                    cost[r2, r2//2] += cmd[-1]
                    r2 //= 2
        else:
            ans = 0
            r1, r2 = cmd[1], cmd[2]
            while r1 != r2:
                if r1 > r2:
                    ans += cost[r1//2, r1]
                    r1 //= 2
                else:
                    ans += cost[r2//2, r2]
                    r2 //= 2
            print(ans)
            

    

solve()
