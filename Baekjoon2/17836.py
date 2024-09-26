from collections import deque

N, M, T = list(map(int, input().split()))


board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


gram = tuple()
record = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            gram = (i, j)


queue = deque([(0, 0)])
visited = [[False] * M for _ in range(N)]
visited[0][0] = True
while queue:
    cx, cy = queue.popleft()

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if (
            0 <= nx < N
            and 0 <= ny < M
            and not visited[nx][ny]
            and (board[nx][ny] == 0 or board[nx][ny] == 2)
        ):
            record[nx][ny] = record[cx][cy] + 1
            visited[nx][ny] = True
            queue.append((nx, ny))


gx, gy = gram

minT = min(record[N - 1][M - 1], record[gx][gy] + abs(N - 1 - gx) + abs(M - 1 - gy))

if minT > T:
    print("Fail")
elif minT == 0:
    if record[gx][gy] == 0:
        print("Fail")
    else:
        if record[gx][gy] + abs(N - 1 - gx) + abs(M - 1 - gy) > T:
            print("Fail")
        else:
            print(record[gx][gy] + abs(N - 1 - gx) + abs(M - 1 - gy))
else:
    print(minT)
