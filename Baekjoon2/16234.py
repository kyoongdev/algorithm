from collections import deque

N, L, R = list(map(int, input().split()))


countries = []

for _ in range(N):
    countries.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(countries, visited, start):

    sx, sy = start

    result = []
    if visited[sx][sy]:
        return result
    visited[sx][sy] = True

    queue = deque([(sx, sy)])

    result.append((sx, sy))

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < N
                and not visited[nx][ny]
                and L <= abs(countries[cx][cy] - countries[nx][ny]) <= R
            ):
                visited[nx][ny] = True
                result.append((nx, ny))
                queue.append((nx, ny))
    return result


people = 0

while True:
    visited = [[False] * N for i in range(N)]
    targets = []
    for x in range(N):
        for y in range(N):
            result = bfs(countries, visited, (x, y))
            if len(result) > 1:
                targets.append(result)
    if len(targets) == 0:
        break

    for sumTargets in targets:
        average = int(sum([countries[x][y] for x, y in sumTargets]) / len(sumTargets))

        for x, y in sumTargets:
            countries[x][y] = average
    # print("-=-=-=-=-=-")
    # for i in range(N):
    #     print(*countries[i])
    people += 1


print(people)
