import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    grid = [IL() for _ in range(n)]
    ans = []
    for i in range(n):
        mask = pow(2, 30) - 1
        for j in range(n):
            if i != j:
                mask &= grid[i][j]
        ans.append(mask)
    for i in range(n):
        for j in range(n):
            if i != j and ans[i] | ans[j] != grid[i][j]:
                print("NO")
                return
    print("YES")
    print(*ans)

for _ in range(II()):
    solve()
