import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    a = IL()
   
    que = deque()
    for num in range(pow(2, n), pow(2, n + 1)):
        que.append(num)
    ans = 0
    idc = defaultdict(list)
    while que:
        node = que.popleft()
        val = 0
        if node in idc:
            # print(node)
            ans += abs(idc[node][1] - idc[node][0])
            val = max(idc[node][1] , idc[node][0])
        par = node // 2
        idc[par].append(a[node - 2] + val)
        if node & 1 and node > 1:
            que.append(par)
    print(ans)  
    

solve()
