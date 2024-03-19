from collections import deque

N, M = list(map(int, input().split()))
r, c, d = tuple(map(int, input().split()))

robots = []
for _ in range(N):
    robots.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
"""
0 : 북
1 : 동
2 : 남
3 : 서
"""


def bfs(start):
    global robots, visited
    x, y, d = start
    queue = deque([start])

    while queue:
        x, y, d = queue.popleft()
        visited[x][y] = True
        isPassed = False
        isExists = False
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < M
                and robots[nx][ny] != 1
                and not visited[nx][ny]
            ):
                isExists = True
        # print(x, y, d, isExists)
        if isExists:
            ## 회전하고
            if d == 0:
                d = 3
            else:
                d -= 1

            ## 바라보는 칸 계산
            nx, ny = x, y
            if d == 0:
                nx -= 1
            elif d == 1:
                ny += 1
            elif d == 2:
                nx += 1
            else:
                ny -= 1

            if robots[nx][ny] == 0 and not visited[nx][ny]:
                queue.append((nx, ny, d))
            else:

                if robots[x][y] == 1:
                    break

                queue.append((x, y, d))
        else:
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            else:
                y += 1
            if robots[x][y] == 1:
                break
            else:

                queue.append((x, y, d))


visited = [[False] * M for _ in range(N)]
bfs((r, c, d))
count = 0
for vi in visited:
    for v in vi:
        if v:
            count += 1

print(count)
