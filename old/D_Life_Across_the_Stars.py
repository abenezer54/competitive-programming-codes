from collections import defaultdict

n = int(input())
linesweep = defaultdict(int)

for _ in range(n):
    birth, death = map(int, input().split())
    linesweep[birth] += 1
    linesweep[death] -= 1

years = []
for key, val in linesweep.items():
    years.append(key)

years.sort()

for i in range(1, len(years)):
    linesweep[years[i]] += linesweep[years[i - 1]]

year = 0
max_people = 0

for i in range(len(years) - 1):
    cur_year = years[i]
    cur_people = linesweep[cur_year]
    if cur_people > max_people:
        max_people = cur_people
        year = cur_year

print(year, max_people)

    