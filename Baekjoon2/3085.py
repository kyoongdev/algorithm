import copy

N = int(input())
boards = [list(input()) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0


def check(newBoards):
    global answer

    for x in range(N):
        # 가로로 연속된 사탕 개수 찾기
        hori_count = 1
        for y in range(1, N):
            if newBoards[x][y] == newBoards[x][y - 1]:
                hori_count += 1
                answer = max(answer, hori_count)
            else:
                hori_count = 1

        # 세로로 연속된 사탕 개수 찾기
        verti_count = 1
        for y in range(1, N):
            if newBoards[y][x] == newBoards[y - 1][x]:
                verti_count += 1
                answer = max(answer, verti_count)
            else:
                verti_count = 1


for x in range(N):
    for y in range(N):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and boards[x][y] != boards[nx][ny]:
                newBoards = copy.deepcopy(boards)
                newBoards[x][y], newBoards[nx][ny] = newBoards[nx][ny], newBoards[x][y]
                check(newBoards)

print(answer)
