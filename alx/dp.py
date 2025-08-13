import os, sys
from collections import defaultdict
# sys.stdin = open("lightbulbs.in", "r")
# sys.stdout = open("lightbulbs.out", 'w')

input = lambda: sys.stdin.readline().strip()

n, k = list(map(int, input().split()))
yellow = list(map(int, input().split()))
blue = list(map(int, input().split()))
ans = -1
memo = {}
def dp(idx, cy, cb):
    # print(idx, cy)
    if idx == n:
        if cy >= k:
            return cb
        return -1
    if (idx, cy, cb) in memo:
        return memo[(idx, cy, cb)]
    
    
    v1 = dp(idx + 1, cy + yellow[idx], cb)
    v2 = dp(idx + 1, cy , cb + blue[idx])
    memo[(idx, cy, cb)] = max(v1, v2)
    return memo[(idx, cy, cb)]
ans = dp(0, 0, 0)
# print(memo)
print(ans)



