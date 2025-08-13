s = input()
a = []
for i in range(len(s)):
    if s[i] == '|':
        a.append(i)
ans = []
for i in range(len(a) - 1):
    ans.append(a[i + 1] - a[i] - 1)
print(*ans)