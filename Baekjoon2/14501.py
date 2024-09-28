from itertools import combinations

N = int(input())
answer = 0
days = []

for _ in range(N):
    days.append(list(map(int, input().split())))


combis = []
for i in range(1, N + 1):
    tmp = []

    for c in combinations(range(N), i):
        tmp.append(list(c))
    combis.extend(tmp)

for combi in combis:
    profit = 0

    combiList = list(combi)
    isOk = True
    for c in combiList:

        day = days[c]

        for i in range(c + 1, day[0] + c):

            if i in combiList:
                isOk = False
        if c + day[0] > N:
            isOk = False
        if isOk:
            profit += day[1]

    if isOk:
        # print(combiList, profit, isOk)
        answer = max(answer, profit)

print(answer)
