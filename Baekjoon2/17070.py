N = int(input())

homes = []

for _ in range(N):
    homes.append(list(map(int, input().split(" "))))


dp = [[[0 for i in range(N)] for i in range(N)] for _ in range(3)]
# 0 가로 1 세로 2 대각선

dp[0][0][1] = 1


for i in range(2, N):
    if homes[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for i in range(1, N):
    for j in range(1, N):
        if homes[i][j] == 0 and homes[i - 1][j] == 0 and homes[i][j - 1] == 0:
            dp[2][i][j] = (
                dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]
            )

        if homes[i][j] == 0:
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]


print(dp[0][N - 1][N - 1] + dp[1][N - 1][N - 1] + dp[2][N - 1][N - 1])
