n = int(input())
s = input()
index = 0
answer = ''
for i in range(1, 55):
    index += i
    if index - 1 < n:
        answer += s[index - 1]
print(answer)
