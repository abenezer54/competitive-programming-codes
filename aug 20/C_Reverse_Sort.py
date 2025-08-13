import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = II()
    s = S()
    # print(s, sorted(s))
    if list(s) == sorted(s):
        # print('yes')
        print(0)
        return
    cnt = s.count('1')
    one = 0
    ans = []
    cur = []
    zero = 0
    flag = False
    for i in range(n - 1, -1, -1):
        # print(cur)
        if not flag:
            if s[i] == '0':
                zero += 1
                cur.append(i + 1)
            else:
                one += 1
                flag = True
                zero -= 1
                cur.append(i + 1)
                if zero == 0 or one == cnt:
                    ans.append(cur[::-1])
                    cur = []
                    flag = False
        else:
            if s[i] == '1':
                one += 1
                zero -= 1
                cur.append(i + 1)
                if zero == 0 or one == cnt:
                    ans.append(cur[::-1])
                    cur = []
                    flag = False
    print(len(ans),)
    for row in ans:
        print(len(row), *row)
    
        
        
for _ in range(II()):
    solve()
