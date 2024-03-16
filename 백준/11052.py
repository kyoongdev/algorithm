N = int(input())
cards =[0] 
cards += list(map(int,input().split(" ")))

dp = [0] * (N + 1)

dp[1] = cards[1]
dp[2] = max(cards[2] , cards[1] * 2)



## 각 카드 개수
for i in range(2,N+1):
  ## 이전 카드
  for j in range(1,i + 1):
    dp[i] = max(dp[i], dp[i - j] + cards[j])

print(dp[N])

"""
i = 3
j => 1, 2, 3
i-j => 2, 1
"""

