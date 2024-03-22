N,K = list(map(int,input().split()))

coins = []
for _ in range(N):
  coins.append(int(input()))

dp  = [10001] * ( K + 1)
dp[0] = 0

# dp[k] : k원으로 만들 수 있는 조합의 개수
# 각 동전
for coin in coins:
  # 가격
  for i in range(coin,K + 1):
    
    dp[i] = min(dp[i - coin]+ 1, dp[i ]) 
if dp[K] == 10001:
  print(-1)
else: print(dp[K])