N,K = list(map(int,input().split(" ")))



items = [[0,0]]

for _ in range(N):
  items.append(list(map(int,input().split(" "))))

backpack = [[0] * (K + 1) for _ in range(N + 1)]

for n in range(1,N + 1):
  for k in range(1,K + 1):
    w = items[n][0]
    v = items[n][1]

    if w > k:
      backpack[n][k] = backpack[n-1][k]
    else:
      backpack[n][k]= max(backpack[n-1][k], backpack[n-1][k-w] + v)


print(backpack[N][K])