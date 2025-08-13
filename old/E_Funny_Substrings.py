import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    prev = defaultdict(int)
    last_three = defaultdict(str)
    first_three = defaultdict(str)
    last = -1
    for _ in range(n):
        x = S()
        # print(last_three)
        if ':' in x:
            left, right = x.split(":")
            left = left[:-1]
            right = right[2:]
            cur = 0
            for i in range(len(right)):
                if right[i:i + 4] == 'haha':
                    cur += 1
            prev[left] = cur
            if len(right) <= 3:
                last_three[left] = right
                first_three[left] = right
            else:
                first_three[left] = right[:3]
                right = right[::-1]
                right = right[:3]
                right = right[::-1]
                last_three[left] = right
            last = left
        else:
            left, right = x.split('+')
            l, mid = left.split('=')
            l = l[:-1]
            mid = mid[1:-1]
            right = right[1:]
            cur = prev[mid] + prev[right]
            s = last_three[mid]
            t = first_three[right]
            for i in range(len(s)):
                x = s[i: i + 4]
                j = 0
                while len(x) < 4 and j < len(t):
                    x += t[j]
                    j += 1
                if x == 'haha':
                    cur += 1

            prev[l] = cur
            tt = first_three[right]
            ss = first_three[mid]
            ft = ''
            i = 0
            while len(ft) < 3 and i < len(ss):
                ft += ss[i]
                i += 1
            i = 0
            while len(ft) < 3 and i < len(tt):
                ft += tt[i]
                i += 1
            first_three[l] = ft
            t = last_three[right]
            t = t[::-1]
            s = s[::-1]
            j = 0
            while len(t) < 3 and j < len(s):
                t += s[j]
                j += 1
            last_three[l] = t[::-1]
            last = l
    print(prev[last])
    



tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()