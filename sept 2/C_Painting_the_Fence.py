import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, q = IL()
    pair = [IL() for _ in range(q)]
    prefix = [0] * (n + 2)

    for l, r in pair:
        prefix[l] += 1
        prefix[r + 1] -= 1
    for i in range(1, n + 2):
        prefix[i] += prefix[i - 1]
    
    # print(prefix)
    cnt = [[0, 0] for _ in range(n + 2)]
    for i in range(1, n + 2):
        cnt[i][0] += cnt[i - 1][0]
        cnt[i][1] += cnt[i - 1][1]
        if prefix[i] == 1:
            cnt[i][0] += 1
        if prefix[i] == 2:
            cnt[i][1] += 1


    off =  prefix[1:-1].count(0)
    possible = n - off
    ans = 0

    for i in range(q):
        for j in range(i + 1, q):
            x, y = pair[i][0], pair[i][1]
            l, r = pair[j][0], pair[j][1]
            arr = sorted([(x, y), (l, r)])
            first_left, first_right = arr[0][0], arr[0][1]
            second_left, second_right = arr[1][0], arr[1][1]
            # if they intersect
            if first_right >= second_left:
                # full intersection 
                if second_right <= first_right:
                    first_pair = (first_left, second_left - 1)
                    mid_pair = (second_left, second_right)
                    second_pair = (second_right + 1, first_right)

                # partial intersection
                else:
                    first_pair = (first_left, second_left - 1)
                    mid_pair = (second_left, first_right)
                    second_pair = (first_right + 1, second_right)
                
            # if there is no intersection
            else:
                first_pair = (first_left, first_right)
                mid_pair = (1, -1) # not valid pair
                second_pair = (second_left, second_right)

            fence_without_color = 0
            if first_pair[0] <= first_pair[1]:
                left = cnt[first_pair[0] - 1][0]
                right = cnt[first_pair[1]][0]
                fence_without_color += right - left

            if mid_pair[0] <= mid_pair[1]:
                # ones
                left = cnt[mid_pair[0] - 1][0]
                right = cnt[mid_pair[1]][0]
                fence_without_color += right - left
                
                # twos
                left = cnt[mid_pair[0] - 1][1]
                right = cnt[mid_pair[1]][1]
                fence_without_color += right - left

            if second_pair[0] <= second_pair[1]:
                left = cnt[second_pair[0] - 1][0]
                right = cnt[second_pair[1]][0]
                fence_without_color += right - left

            ans = max(ans, possible - fence_without_color)
    print(ans)     

solve()
