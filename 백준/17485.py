import sys

input = sys.stdin.readline
INF = 1e10

N, M = list(map(int, input().split()))

maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

direction = [(1, -1), (1, 0), (1, 1)]

dp = [[[0] * 3 for _ in range(M)] for _ in range(N)]
for j in range(M):
    for k in range(3):
        dp[0][j][k] = maps[0][j]


for x in range(1, N):
    for y in range(M):
        for k in range(3):
            if (y == 0 and k == 0) or (y == M - 1 and k == 2):
                dp[x][y][k] = INF
                continue
            if k == 0:
                dp[x][y][k] = maps[x][y] + min(dp[x - 1][y - 1][1], dp[x - 1][y - 1][2])
            elif k == 1:
                dp[x][y][k] = maps[x][y] + min(dp[x - 1][y][0], dp[x - 1][y][2])
            else:
                dp[x][y][k] = maps[x][y] + min(dp[x - 1][y + 1][0], dp[x - 1][y + 1][1])


result = INF
for j in range(M):
    result = min(result, min(dp[-1][j]))
print(result)
