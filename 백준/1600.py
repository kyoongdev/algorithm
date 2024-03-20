from collections import deque

K = int(input())
W, H = list(map(int, input().split()))

maps = []
for _ in range(H):
    maps.append(list(map(int, input().split())))

for x in range(H):
    for y in range(W):
        if maps[x][y] == 1:
            maps[x][y] = -1

horse = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
maxHorseCount = K


visited = [[[False] * (K+1) for _ in range(W)] for _ in range(H)]

result = -1
start = (0, 0)
queue = deque([(0,0,K,0)])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x,y,k,move = queue.popleft()

    if x == H -1 and y == W - 1:
        result = move
        break

    if k:
        for hx,hy in horse:
            nx,ny = x + hx, y + hy

            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny][k - 1] and maps[nx][ny] != -1:
                visited[nx][ny][k -1] = True
                queue.append((nx,ny,k-1,move +1))
    for i in range(4):
        nx,ny = x + dx[i], y + dy[i]

        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny][k] and maps[nx][ny] != -1:
            visited[nx][ny][k]= True
            queue.append((nx,ny,k,move + 1))

print(result)
    