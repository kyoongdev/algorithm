import sys
input = sys.stdin.readline

T = int(input())
K = int(input())

coins = []
M = 0
dp = [0] * ( T + 1) 
dp[0] = 1
for _ in range(K):
  coin,cnt =  list(map(int,input().split()))
  # coins.append((p,n))
  for money in range(T,0,-1):
    for i in range(1, cnt + 1):
      if money  - coin * i >= 0:
        dp[money] += dp[money - i * coin]


# dp[k] 는 k원으로 만들 수 있는 동전 조합의 수


  

print(dp[T])
    



