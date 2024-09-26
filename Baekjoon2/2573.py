from collections import deque
import copy

N, M = list(map(int, input().split()))

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def melt():
    global arr
    tmpArr = copy.deepcopy(arr)
    targets = []
    for x in range(N):
        for y in range(M):
            if arr[x][y] != 0:
                meltCount = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                        meltCount += 1
                if meltCount > arr[x][y]:
                    tmpArr[x][y] = 0
                else:
                    tmpArr[x][y] -= meltCount

                if tmpArr[x][y] != 0:
                    targets.append((x, y))

    return tmpArr, targets


def search(targets):
    global arr
    groups = 0
    visited = [[False] * M for _ in range(N)]

    for target in targets:
        queue = deque([target])

        x, y = target
        if visited[x][y]:
            continue
        groups += 1
        if groups >= 2:
            return groups
        visited[x][y] = True
        while queue:
            cx, cy = queue.popleft()

            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if (
                    0 <= nx < N
                    and 0 <= ny < M
                    and not visited[nx][ny]
                    and arr[nx][ny] != 0
                ):

                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return groups


year = 0

while True:
    year += 1
    newArr, targets = melt()
    if len(targets) == 0:
        year = 0
        break
    arr = newArr
    groups = search(targets)

    if groups >= 2:
        break

print(year)
