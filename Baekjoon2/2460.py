currentPeople = 0
maxPeople = 0
for i in range(10):
    minus, add = map(int, input().split())

    currentPeople += add
    currentPeople -= minus
    maxPeople = max(currentPeople, maxPeople)

print(maxPeople)
