import sys
input = sys.stdin.readline

N,K = list(map(int,input().split()))

dp = [0] * (K + 1)
dp[0] = 1
coins = []
for i in range(N):
  coin = int(input())
  coins.append(coin)

for c in coins:

  for j in range(c,K + 1):    
    dp[j] += dp[j - c]

        
  
print(dp[K])