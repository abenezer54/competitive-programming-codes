import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
sint = lambda: int(input())

def solve():
    def printQry(a, b) -> int:
        sa = str(a)
        sb = str(b)
        print(f"? {sa} {sb}", flush = True)
        return sint()
    def printAns(ans) -> None:
        ans  = ' '.join(ans)
        print(f"! {ans}", flush = True)
    n = II()
    vis = set()
    ans = []
    cnt = 0
    que = deque()
    vis2 = set()
    for v in range(2, n + 1):
        val = printQry(1, v)
        if (v, 1) not in vis and val == 1:
            cnt += 1
            vis.add((1, v))
            vis.add((v, 1))
            ans.append(str(v))
            ans.append(str(1))
        else:
            if not (v, 1) in vis2:
                que.append((val, v))
                que.append((1, val))
                vis2.add((val, v))
                vis2.add((1, val))
    while cnt < n - 1 and que:
        v, u = que.popleft()
        val = printQry(u, v)
        if v != u and (v, u) not in vis and val == u :
            vis.add((u, v))
            vis.add((v, u))
            ans.append(str(v))
            ans.append(str(u))
        else:
            if not (v, u) in vis2:
                que.append((v, val))
                que.append((val, u))
                vis2.add((v, val))
                vis.add((val, u))
    printAns(ans)
for _ in range(II()):
    solve()
