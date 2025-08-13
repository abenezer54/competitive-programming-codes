import sys, os
input = lambda: sys.stdin.readline().strip()

t = int(input())
while t:
    n = int(input())
    val = 1 << (n.bit_length() - 1)
    diff = n - val + 1
    print('diff', diff)
    if n & 1:
        print(n)
    else:
        print((2 * val) - 1)
        
    t -= 1