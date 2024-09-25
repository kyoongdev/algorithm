N = 19

maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))


dx = [1, 1, 0, -1]
dy = [0, 1, 1, 1]


def check():
    global maps

    for x in range(N):
        for y in range(N):
            if maps[x][y] == 1 or maps[x][y] == 2:

                focus = maps[x][y]

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    count = 1

                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue

                    while 0 <= nx < N and 0 <= ny < N and maps[nx][ny] == focus:
                        count += 1

                        if count == 5:
                            if (
                                0 <= nx + dx[i] < N
                                and 0 <= ny + dy[i] < N
                                and maps[nx + dx[i]][ny + dy[i]] == focus
                            ):
                                break

                            if (
                                0 <= x - dx[i] < N
                                and 0 <= y - dy[i] < N
                                and maps[x - dx[i]][y - dy[i]] == focus
                            ):
                                break

                            return focus, x + 1, y + 1

                        nx += dx[i]
                        ny += dy[i]

    return -1, 0, 0


focus, x, y = check()

if focus == -1:
    print(0)
else:
    print(focus)
    print(x, y)
