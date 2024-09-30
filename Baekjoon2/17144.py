R, C, T = list(map(int, input().split()))

maps = []
cleanerPoint = []
for x in range(R):
    line = list(map(int, input().split()))
    for y in range(C):
        if line[y] == -1:
            cleanerPoint.append((x, y))
    maps.append(line)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cleanerPoint.sort()


def spread():
    global maps

    targets = []
    newMaps = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if maps[x][y] != 0 and maps[x][y] != -1:
                targets.append((x, y))

    for cx, cy in cleanerPoint:
        newMaps[cx][cy] = -1
    for tx, ty in targets:
        spreadTargets = []
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if 0 <= nx < R and 0 <= ny < C and maps[nx][ny] != -1:
                spreadTargets.append((nx, ny))

        if len(spreadTargets) > 0:
            A = int(maps[tx][ty] / 5)
            newMaps[tx][ty] += max(0, maps[tx][ty] - (A * len(spreadTargets)))
            # print(tx, ty, A, maps[tx][ty] - (A * len(spreadTargets)))
            for sx, sy in spreadTargets:
                newMaps[sx][sy] += A
    maps = newMaps


def cleaner():

    ux, uy = cleanerPoint[0]
    dx, dy = cleanerPoint[1]

    ##위쪽 껍데기
    uUp = maps[0][: C - 1]
    uRight = [maps[x][-1] for x in range(ux)]
    uDown = maps[ux][1:][::-1]
    uLeft = [maps[x][0] for x in range(1, ux + 1)][::-1]

    ##아래쪽 껍데기
    dUp = maps[dx][: C - 1]
    dRight = [maps[x][-1] for x in range(dx, R - 1)]
    dDown = maps[R - 1][1:][::-1]
    dLeft = [maps[x][0] for x in range(dx + 1, R)][::-1]

    upList = uUp + uRight + uDown + uLeft
    downList = dUp + dRight + dDown + dLeft

    upList.append(upList.pop(0))
    downList.insert(0, downList.pop())

    # 위쪽 껍데기 다시 넣기
    idx = 0

    # 위쪽 껍데기의 상단 (uUp)
    for i in range(C - 1):
        maps[0][i] = upList[idx]
        idx += 1

    # 위쪽 껍데기의 오른쪽 (uRight)
    for i in range(ux):
        maps[i][-1] = upList[idx]
        idx += 1

    # 위쪽 껍데기의 하단 (uDown)
    for i in range(C - 1, 0, -1):
        maps[ux][i] = upList[idx]
        idx += 1

    # 위쪽 껍데기의 왼쪽 (uLeft)
    for i in range(ux, 0, -1):
        maps[i][0] = upList[idx]
        idx += 1

    # 아래쪽 껍데기 다시 넣기
    idx = 0

    # 아래쪽 껍데기의 상단 (dUp)
    for i in range(C - 1):
        maps[dx][i] = downList[idx]
        idx += 1

    # 아래쪽 껍데기의 오른쪽 (dRight)
    for i in range(dx, R - 1):
        maps[i][-1] = downList[idx]
        idx += 1

    # 아래쪽 껍데기의 하단 (dDown)
    for i in range(C - 1, 0, -1):
        maps[R - 1][i] = downList[idx]
        idx += 1

    # 아래쪽 껍데기의 왼쪽 (dLeft)
    for i in range(R - 1, dx, -1):
        maps[i][0] = downList[idx]
        idx += 1

    maps[dx][1] = 0
    maps[ux][1] = 0

    for sx, sy in cleanerPoint:
        maps[sx][sy] = -1


for i in range(T):
    spread()
    cleaner()

answer = 0

for x in range(R):

    for y in range(C):
        if maps[x][y] != -1:
            answer += maps[x][y]


print(answer)
