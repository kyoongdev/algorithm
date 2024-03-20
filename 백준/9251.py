lineOne = input()
lineTwo = input()

dp = [[0] * (len(lineTwo) + 1) for _ in range(len(lineOne) + 1)]

for i in range(1, len(lineOne) + 1):
    for j in range(1, len(lineTwo) + 1):
        print(i, j, lineOne[i - 1], lineTwo[j - 1])
        if lineOne[i - 1] == lineTwo[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
