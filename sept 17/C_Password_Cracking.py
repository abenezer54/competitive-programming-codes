import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
sint = lambda: int(input())


def solve():
    def printQry(t) -> int:
        print(f"? {t}", flush = True)
        return II()
    
    def printAns(ans) -> None:
        print(f"! {ans}", flush = True)

    n = II()
    # only forward
    cur = deque([])
    start = 0
    flag = False
    while len(cur) != n:

        #op 1
        cur.append("1")
        t = ''.join(cur)
        res = printQry(t)
        if res == 1:
            if not flag:
                start = 1
                flag = True
            continue
        else:
            cur.pop()
            cur.append("0")
            t = ''.join(cur)
            if printQry(t) == 1:
                continue
            else:
                cur.pop()
                break
    # only backward
    if len(cur) < n:
        if start:
            cur.appendleft('0')
        else:
            cur.appendleft('1')


    while len(cur) != n:
        cur.appendleft('1')
        t = ''.join(cur)
        if printQry(t) == 1:
            continue
        else:
            cur.popleft()
            cur.appendleft("0")
            t = ''.join(cur)
            if printQry(t) == 1:
                continue
            else:
                cur.popleft()
                break
    printAns(''.join(cur))





for _ in range(II()):
    solve()
