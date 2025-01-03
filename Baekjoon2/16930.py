from collections import deque

N, M, K = map(int, input().split())

gyms = []

for _ in range(N):
    gyms.append(input())

x1, y1, x2, y2 = map(int, input().split())

visited = [[float("inf") for i in range(M)] for i in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


queue = deque([(x1 - 1, y1 - 1, 0)])

minK = min(K, N)
minK = min(minK, M)

while queue:
    cx, cy, ct = queue.popleft()
    if cx == x2 - 1 and cy == y2 - 1:
        break

    for i in range(4):
        for k in range(1, minK + 1):

            nx = cx + k * dx[i]
            ny = cy + k * dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break

            if gyms[nx][ny] == "#":
                break

            if visited[nx][ny] <= ct:
                break

            if visited[nx][ny] > ct + 1:
                visited[nx][ny] = ct + 1
                queue.append((nx, ny, ct + 1))


if visited[x2 - 1][y2 - 1] == float("inf"):
    print(-1)
else:
    print(visited[x2 - 1][y2 - 1])


"""
3 4 4
....
#.#.
....
1 1 3 1
"""
