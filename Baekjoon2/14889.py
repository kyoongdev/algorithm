from itertools import combinations

N = int(input())


ablis = []
for i in range(N):

    ablis.append(list(map(int, input().split())))


def getScore(team):
    global ablis
    score = 0
    for x, y in combinations(team, 2):
        score += ablis[x][y] + ablis[y][x]

    return score


players = [i for i in range(N)]
startTeamCombi = combinations(players, N // 2)

minDiff = float("inf")

for startTeam in startTeamCombi:
    linkTeam = [p for p in players if p not in list(startTeam)]
    sScore = getScore(startTeam)
    lScore = getScore(linkTeam)

    minDiff = min(minDiff, abs(sScore - lScore))


print(minDiff)
