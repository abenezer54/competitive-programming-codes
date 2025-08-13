import sys, os, heapq
from collections import defaultdict, Counter
input = lambda: sys.stdin.readline().strip()
IL = lambda:  list(map(int, input().split()))
MOD = int(1e9) + 7
t = int(input())
while t:
    n = int(input())
    a = IL()
    ans = [0] * n
    prev = 0
    cnt = sm = 0
    mx = 1
    for i in range(n):
        if a[i] > mx:
            ans[i] = (sm + ((mx * ((1 << (cnt + prev)) % MOD)) % MOD)) % MOD
            # mx = 
        # else:


        while a[i] % 2 == 0:
            a[i] //= 2
            cnt += 1
        
        
    print(ans)

        
    t -= 1