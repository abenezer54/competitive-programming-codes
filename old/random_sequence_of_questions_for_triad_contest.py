from random import randint

questions = list(range(1, 10))

result = []
for _ in range(9):
    idx = randint(0, len(questions) - 1)
    result.append(questions.pop(idx))
print(result)
# [5, 6, 2, 4, 9, 7, 1, 8, 3]