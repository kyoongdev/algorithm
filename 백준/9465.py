T = int(input())



for _ in range(T):
  N = int(input())
  sticker1,sticker2 = [[0,*list(map(int,input().split(" ")))],[0,*list(map(int,input().split(" ")))]]

  if N < 2:
    print(max(sticker1[0]+ sticker2[1], sticker1[1] + sticker2[0]))
  else:
    dp = [[0,0] for _ in range(N + 1)]
    
    dp[1] = [sticker1[1], sticker2[1]]

    for i in range(2,N + 1):
      dp[i] = [sticker1[i] + max(dp[i-2][1], dp[i-1][1]), sticker2[i] + max(dp[i-2][0] , dp[i-1][0])]      
    
    print(max(dp[-1]))






