import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def ask(l, r):
    print("?", l, r, flush=True)
    res = IL()[0]
    return res
def response(ans):
    print("!", ans, flush=True)

def solve():
    n = IL()[0]

    if n == 2:
        res = ask(1, 2)
        if res == 0:
            response("IMPOSSIBLE")
        else:
            response("01")
        return 
    ans = []

    left = 2
    prev = ask(1, n)
    first = prev
    if prev == 0:
        response("IMPOSSIBLE")
        return
    for _ in range(n - 2):
        res = ask(left, n)
        if res < prev:
            ans.append('0')
        else:
            ans.append('1')
        if res == 0:
            ans.append('1')
            break
        prev = res
        left += 1
    if n - len(ans) == 2 and res:
        ans.extend(['0', '1'])
        response(''.join(ans))
        return
    
    prev = first
    x = []
    val = 1
    for _ in range(n - len(ans)):
        res = ask(1, n - val)
        if res < prev:
            x.append('1')
        else:
            x.append('0')
        val += 1
        prev = res

    x.reverse()
    ans.extend(x)
    response(''.join(ans))


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()