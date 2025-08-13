import sys, math, random; from heapq import heapify, heappop, heappush;
from collections import defaultdict, Counter, deque; from bisect import bisect_left, bisect_right
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = IL()[0]
    a = IL()
    ones = deque()
    zeros = deque()
    twos = deque()

    for i in range(n):
        if a[i] == 0:
            zeros.append(i + 1)
        elif a[i] == 1:
            ones.append(i + 1)
        else:
            twos.append(i + 1)

    ans = []
    hold_one = deque()
    hold_zero = deque()

    while ones and zeros and ones[0] < zeros[-1]:
        x = ones.popleft()
        y = zeros.pop()
        ans.append((x, y))
        hold_one.append(y)
        hold_zero.append(x)

    ones.extend(hold_one)
    zeros.extend(hold_zero)
    ones = deque(sorted(ones))
    zeros = deque(sorted(zeros))

    hold_one = deque()
    while twos and ones and twos[0] < ones[-1]:
        x = twos.popleft()
        y = ones.pop()
        hold_one.append(x)
        ans.append((x, y))

    ones.extend(hold_one)
    ones = deque(sorted(ones))
    while ones and zeros and ones[0] < zeros[-1]:
        x = ones.popleft()
        y = zeros.pop()
        ans.append((x, y))
    # print(ans)
    assert len(ans) <= n
    print(len(ans))

    
    for val in ans:
        print(*val)


tt = 1
tt = IL()[0]
for _ in range(tt):
    solve()
def find_divisors(number):
    divisors = []
    limit = int(number**0.5) + 1
    for i in range(1, limit):
        if number % i == 0:
            divisors.append(i)
            complement = number // i
            if i != complement:
                divisors.append(complement)
    return divisors