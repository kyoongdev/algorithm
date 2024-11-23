from itertools import combinations

littles = []

for i in range(9):
    littles.append(int(input()))

candis = combinations(littles, 7)

for c in candis:
    if sum(c) == 100:
        answer = list(c)
        answer.sort()
        for i in answer:
            print(i)
        break
