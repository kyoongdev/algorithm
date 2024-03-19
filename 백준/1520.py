import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def dfs(x, y):

    if x == M - 1 and y == N - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    way = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and maps[nx][ny] < maps[x][y]:
            way += dfs(nx, ny)
    dp[x][y] = way
    return dp[x][y]


M, N = list(map(int, input().split()))

maps = [list(map(int, input().split())) for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


dp = [[-1] * N for _ in range(M)]

print(dfs(0, 0))
