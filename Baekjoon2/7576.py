from collections import deque

M, N = list(map(int, input().split()))

tomato = []

for _ in range(N):
    tomato.append(list(map(int, input().split())))


tomatoCount = 0
startPoints = []
oneTomatos = []
zeroCount = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1 or tomato[i][j] == 0:
            tomatoCount += 1
            if tomato[i][j] == 1:

                oneTomatos.append((i, j))
                startPoints.append((i, j))
            else:
                zeroCount += 1


if zeroCount == 0:
    print(0)
    exit()


def countTomato():
    global tomato
    count = 0
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                count += 1

    return count


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * M for _ in range(N)]
for startX, startY in startPoints:
    q = deque([(startX, startY)])
    visited[startX][startY] = True

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if (
                0 <= nx < N
                and 0 <= ny < M
                and not visited[nx][ny]
                and tomato[nx][ny] != -1
            ):
                visited[nx][ny] = True
                q.append((nx, ny))


visitCount = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            visitCount += 1


if visitCount != tomatoCount:
    print(-1)
    exit()


q2 = deque([oneTomatos])
day = 0
while q2:
    ts = q2.popleft()

    newTs = []
    for tx, ty in ts:

        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = 1
                newTs.append((nx, ny))

    if len(newTs) > 0:
        day += 1
        q2.append(newTs)


print(day)
