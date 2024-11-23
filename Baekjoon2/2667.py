from collections import deque

N = int(input())

danjis = []
for i in range(N):
    danjis.append(list(input()))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * N for i in range(N)]


def bfs(start):
    global dx, dy, danjis, N, visited

    count = 1

    queue = deque([start])

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < N
                and not visited[nx][ny]
                and danjis[nx][ny] != "0"
            ):
                visited[nx][ny] = True
                count += 1
                queue.append((nx, ny))

    return count


counts = []

for x in range(N):
    for y in range(N):
        if not visited[x][y] and danjis[x][y] != "0":

            visited[x][y] = True
            counts.append(bfs((x, y)))

counts.sort()

print(len(counts))
for count in counts:
    print(count)
