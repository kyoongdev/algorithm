from sys import stdin

N = int(stdin.readline())

days = []

for _ in range(N):
    days.append(list(map(int, stdin.readline().split())))

dp = [0] * (N + 1)

if days[N - 1][0] == 1:
    dp[N - 1] = days[N - 1][1]

for i in range(N - 1, -1, -1):
    dpMax = dp[i + 1]

    day = days[i][0]
    cost = days[i][1]

    if day + i <= N:

        dpMax = max(dpMax, dp[i + day] + cost)

    dp[i] = dpMax


print(dp[0])
