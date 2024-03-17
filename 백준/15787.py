def commandOne(i,x):
  global train

  if train[i][x] == 0:
    train[i][x] = 1
    
def commandTwo(i,x):
  global train

  train[i][x] = 1

def commandThree(i):
  global train
  
  skipIndex = -1
  for n in range(0,len(train[i]) - 2):
    if n == skipIndex:
      continue
    if train[i][n] == 1:
      train[i][n+1] = 1
      train[i][n] = 0
      if train[i][n + 1] == 1:
        skipIndex = n + 1

def commandFour(i):
  global train

  skipIndex = -1
  for n in range(len(train[i]) -1, 0, - 1):
    if n == skipIndex:
      continue

    if train[i][n] == 1:
      train[i][n-1] = 1
      train[i][n] = 0
      if train[i][n - 1] == 1:
        skipIndex = n - 1



N,M = list(map(int,input().split(' ')))
commands = []
train = [[0] * 20 for _ in range(N)]

for _ in range(M):
  commands.append(list(map(int,input().split(" "))))

for c in commands:
  target = c[0]
  if target == 1:
    commandOne(c[1]-1,c[2]-1)
  elif target == 2:
    commandTwo(c[1]-1,c[2]-1)
  elif target == 3:
    commandThree(c[1]-1)
  else:
    commandFour(c[1]-1)
exists = []
for t in train:

  if t not in exists and 1 in t:
    exists.append(t)

print(len(exists))
  

"""
5 7
1 1 1
1 1 2
1 2 2
1 2 3
1 3 1
3 1
4 1
"""