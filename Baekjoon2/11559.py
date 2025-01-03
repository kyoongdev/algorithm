from collections import deque

lines = []
for i in range(12):
    lines.append(list(input()))


def bfs(start, visited):
    global lines
    sx, sy = start
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    boom = lines[sx][sy]

    queue = deque([(sx, sy)])

    history = [(sx, sy)]
    visited[sx][sy] = True

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if (
                0 <= nx < 12
                and 0 <= ny < 6
                and not visited[nx][ny]
                and lines[nx][ny] == boom
            ):

                queue.append((nx, ny))
                history.append((nx, ny))
                visited[nx][ny] = True

    return history


def reconcil():
    global lines
    for col in range(6):
        stack = []
        for row in range(11, -1, -1):  # 아래에서 위로 탐색
            if lines[row][col] != ".":
                stack.append(lines[row][col])
        # 열 재구성
        for row in range(11, -1, -1):
            if stack:
                lines[row][col] = stack.pop(0)
            else:
                lines[row][col] = "."


boomCount = 0

while True:
    targets = []
    visited = [[False] * 6 for i in range(12)]

    for x in range(12):
        for y in range(6):
            if lines[x][y] != ".":
                history = bfs((x, y), visited)

                if len(history) >= 4:

                    targets.append(history)

    if len(targets) == 0:
        break

    for target in targets:
        for x, y in target:
            lines[x][y] = "."
    # print("---")
    # for l in lines:
    #     print(l)
    reconcil()
    boomCount += 1
    # print("reconcil")
    # for l in lines:
    #     print(l)


print(boomCount)
"""
......
......
......
......
......
......
.G....
RR....
RY....
RYG...
RRY...
RYYGG.
"""
