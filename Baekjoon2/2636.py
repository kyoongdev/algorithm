from collections import deque

N, M = list(map(int, input().split()))

maps = []

for _ in range(N):
    maps.append(list(map(int, input().split())))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def searchCheese():
    cheese = set()

    start = (0, 0)

    queue = deque([start])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if maps[nx][ny] == 1:
                    cheese.add((nx, ny))

                else:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return cheese


def countAllCheese():

    count = 0

    for x in range(N):
        for y in range(M):
            if maps[x][y] == 1:
                count += 1

    return count


time = 0
rest = 0
while True:

    cheese = searchCheese()
    count = countAllCheese()

    if count == len(cheese):
        rest = len(cheese)
        break

    for cx, cy in cheese:
        maps[cx][cy] = 0

    time += 1


print(time + 1)
print(rest)
