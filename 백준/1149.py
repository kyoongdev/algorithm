

N = int(input())

homes = []
for _ in range(N):
  homes.append(list(map(int, input().split(" "))))


rgbs = [[0] * 3 for _ in range(N + 1)]

for j in range(1,N + 1 ):
  rgbs[j][0] = min(rgbs[j - 1][1],rgbs[j - 1][2]) + homes[j - 1][0]
  rgbs[j][1] = min(rgbs[j - 1][0],rgbs[j - 1][2]) + homes[j - 1][1]
  rgbs[j][2] = min(rgbs[j - 1][1],rgbs[j - 1][0]) + homes[j - 1][2]

print(min(*rgbs[N]))



  
  
    
  




