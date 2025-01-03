result = {}
teams = ["A", "B", "C", "D", "E", "F"]
matches = []
for i in range(6):
    for j in range(i + 1, 6):
        matches.append([teams[i], teams[j]])


pointers = {"A": 0, "B": 3, "C": 6, "D": 9, "E": 12, "F": 15}


def getMatch(depth, records, scores):
    if depth == 15:

        result["".join([str(x) for x in records])] = True
        return

    for i in range(18):
        if records[i] > scores[i]:
            return

    teamA, teamB = matches[depth]
    teamAIdx = pointers[teamA]
    teamBIdx = pointers[teamB]

    # A 승리
    winRecords = records[:]
    winRecords[teamAIdx] += 1
    winRecords[teamBIdx + 2] += 1
    getMatch(depth + 1, winRecords, scores)

    # B 승리
    looseRecords = records[:]
    looseRecords[teamAIdx + 2] += 1
    looseRecords[teamBIdx] += 1
    getMatch(depth + 1, looseRecords, scores)

    # 무승부
    drawRecords = records[:]
    drawRecords[teamAIdx + 1] += 1
    drawRecords[teamBIdx + 1] += 1
    getMatch(depth + 1, drawRecords, scores)


scores = []
for i in range(4):
    score = list(map(int, input().split()))
    scores.append(score)

for s in scores:
    getMatch(0, [0] * 18, s)

    if "".join([str(x) for x in s]) in result:
        print(1, end=" ")
    else:
        print(0, end=" ")
