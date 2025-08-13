import os, sys

sys.stdin = open("dsum.in", "r")
sys.stdout = open("dsum.out", 'w')

input = lambda: sys.stdin.readline().strip()

n = input()
ans = 0
for num in n:
    ans += int(num)

print(ans)