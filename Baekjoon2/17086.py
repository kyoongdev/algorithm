from collections import deque

N, M = map(int, input().split())

spaces = []

for _ in range(N):
    spaces.append(list(map(int, input().split())))


distance = 0


dx = [1, -1, 1, -1, 1, -1, 0, 0]
dy = [1, -1, -1, 1, 0, 0, 1, -1]


def bfs(current):
    global spaces, distance, N, M, dx, dy

    queue = deque([(current[0], current[1])])
    visited = [[0 for i in range(M)] for i in range(N)]

    while queue:
        cx, cy = queue.popleft()

        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if spaces[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[cx][cy] + 1
                else:
                    return visited[cx][cy] + 1


for x in range(N):
    for y in range(M):
        if spaces[x][y] == 0:
            distance = max(distance, bfs([x, y]))

print(distance)

"""
5 4
0 0 1 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
"""
