a, b = [], []
for _ in range(1000):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
import collections as c 
cnt = c.Counter(b)

ans = 0
for i in range(1000):
    ans += a[i] * cnt[a[i]]
print(ans)