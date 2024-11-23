N, K = map(int, input().split())
coins = []

for i in range(N):
    coins.append(int(input()))

coins.sort()

dp = [0] * (K + 1)
dp[0] = 1


for coin in coins:
    for i in range(coin, K + 1):
        dp[i] = dp[i - coin] + dp[i]

print(dp)
"""
3 10
1, 2, 5

1 * 10

2 * 5

5 * 2



"""
