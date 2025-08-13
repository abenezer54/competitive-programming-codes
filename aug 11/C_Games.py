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
    odd = []
    even = []
    for i in range(n):
        if a[i] & 1:
            odd.append(a[i])
        else:
            even.append(a[i])
    even.sort()
    odd.sort()
    al = bob = 0
    for i in range(n):
        if i % 2 == 0:
            if odd:
                if even:
                    if odd[-1] > even[-1]:
                        odd.pop()
                    else:
                        al += even.pop()
                else:
                    odd.pop()
            else:
                al += even.pop()
        else:
            if even:
                if odd:
                    if even[-1] > odd[-1]:
                        even.pop()
                    else:
                        bob += odd.pop()
                else:
                    even.pop()
            else:
                bob += odd.pop()
    if al > bob:
        print("Alice")
    elif al < bob:
        print("Bob")
    else:
        print("Tie")

for _ in range(II()):
    solve()
