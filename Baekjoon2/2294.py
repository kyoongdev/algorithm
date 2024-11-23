N, K = map(int, input().split())

coins = []


dp = [float("inf")] * (K + 1)
dp[0] = 1

for i in range(N):
    coin = int(input())
    coins.append(coin)
    if coin <= K:
        dp[coin] = 1


coins.sort()


for coin in coins:
    # print("coin : ", coin)
    for i in range(coin, K + 1):
        # print("i : ", i)
        # print("dp : ", dp)
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[K] == float("inf"):
    print(-1)
else:
    print(dp[K])

"""
1
5
12
0 1 2 3 4 5 6 7 8 9 10 11 12
1 1       1               1
"""
