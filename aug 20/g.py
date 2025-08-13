n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()


l, r = 0, k + 10

def check(mid):
    if mid > k:
        return False
    val = a[n // 2] + mid
    # print(val)
    need = 0
    for i in range((n // 2) + 1, n):
        # print('i', i)
        x = val - a[i]
        if x > 0:
            need += x
    return need <= k - mid

# print(check(2))
while l + 1 < r:
    mid = (l + r) // 2

    if check(mid):
        l = mid
    else:
        r = mid
print(a[n // 2] + l)





