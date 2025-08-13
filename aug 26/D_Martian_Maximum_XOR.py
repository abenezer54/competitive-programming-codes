import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    a = IL()
    # print(a)
    root = [-1, -1]
    num1 = num2 = -1
    ans = 0
    opp = {"0":"1", "1":"0"}
    for i, num in enumerate(a):
        bits = bin(num)[2:]
        r = k - len(bits) 
        bits = ('0' * r) + bits
        if i != 0:
            # search best option for num
            cur = root
            res = 0
            path = []
            sec = 0
            for (j, bit) in enumerate(bits):
                if cur[int(bit)] != -1:
                    cur = cur[int(bit)]
                    if int(bit):
                        sec |= (1 << (k - j - 1))
                    res |= (1 << (k - j - 1))
                    path.append(bit)
                else:
                    if int(opp[bit]):
                        sec |= (1 << (k - j - 1))
                    cur = cur[int(opp[bit])]
            if res >= ans:
                num1 = num
                num2 = sec
                ans = res
            # print(res)

        # insert to trie
        cur = root
        for bit in bits:
            if cur[int(bit)] == -1:
                cur[int(bit)] = [-1, -1]

            cur = cur[int(bit)]
    # print(~3)
    # print(num1, num2)
    x = 0
    for i in range(k):
        if not ((num1 ^ num2) & (1 << i)):
            if not(num1 & (1 << i)):
                x |= (1 << i)
    idx1 = a.index(num1)
    a.pop(idx1)
    idx2 = a.index(num2)
    if idx2 >= idx1:
        idx2 += 1
    print(*sorted([idx1 + 1, idx2 + 1]),  x)




for _ in range(II()):
    solve()
