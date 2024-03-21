import sys
sys.setrecursionlimit(1111111)
input = sys.stdin.readline



def dfs(start):
  global result
  visits[start] = True
  stds.append(start)
  nextStd = students[start]

  if visits[nextStd]:
    if nextStd in stds:
      # print(stds,stds[stds.index(nextStd):])
      result.extend(stds[stds.index(nextStd):])
    return
  else:
    dfs(nextStd)
  

for _ in range(int(input())):
  N = int(input())
  students = [0]
  students.extend(list(map(int,input().split())))

  visits = [False] * (N + 1)
  visits[0] = True
  result = []
  for idx in range(1, N + 1):
    if not visits[idx]:
      # print(idx)
      stds = []
      dfs(idx)

  # print(visits)
  # print(result)
  print(N - len(result) )





