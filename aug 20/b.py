import math
t = int(input())
while t:
    n = int(input())
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(math.comb(4, 2) % 998244353)
    pmn = min(a[1], b[1])
    pmx = max(a[1], b[1])
    prev = pmx - pmn + 2 + c[1] - 1
    # print(prev)
    ans = prev 
    for i in range(2, n):
        if a[i] == b[i]:
            prev = c[i] + 1
            ans = max(ans, prev)
        else:
            mx = max(a[i], b[i])
            mn = min(a[i], b[i])
            cur = mx - mn + c[i] + 1
            r = mx - mn
            # print('cur', cur, 'r', r)
            if prev:
                x = cur +  prev - (r * 2) 
            cur = max(cur, x)
            prev = cur
            ans = max(ans, cur)
    print(ans)


    t -= 1
