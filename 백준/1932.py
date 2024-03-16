N = int(input())

tri = []

for _ in range(N):
  tri.append(list(map(int,input().split(" "))))


for i in range(1,N):
  triLength = len(tri[i])

  for j in range(triLength):
    if j == 0:
      tri[i][j] += tri[i - 1][0]
    elif j + 1 == triLength:
      tri[i][j] += tri[i - 1][j - 1]
    else:
      tri[i][j] = max(tri[i-1][j], tri[i-1][j - 1]) + tri[i][j]

# print("---")
# for t in tri:
#   print(t)

print(max(tri[-1]))
