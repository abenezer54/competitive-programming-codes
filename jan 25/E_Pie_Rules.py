import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
from types import GeneratorType

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


def solve():
    n = IL()[0]
    a = IL()
    tot = sum(a)
    dp = {}
    # print(type((n, 1)))
    dp[(n, 1)] = 0
    dp[(n, 2)] = 0
    @bootstrap
    def recc(x, i):
        if (x, i) in dp:
            yield dp[(x, i)]
        
        if i == 1:
            y = yield recc(x + 1, 2)
            take = a[x] + y
            leave = yield recc(x + 1, 1)
            dp[(x, i)] = max(take, leave)
        else:
            take = yield recc(x + 1, 1)
            y = yield recc(x + 1, 2)
            leave = a[x] + y
            dp[(x, i)] = min(take, leave)

        yield dp[(x, i)]
    ans = recc(0, 1)
   
    print(tot - ans, ans)
       


tt = 1
# tt = IL()[0]
for _ in range(tt):
    solve()