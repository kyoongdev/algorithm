# link : https://www.acmicpc.net/problem/1697
from collections import deque
N,K = list(map(int,input().split()))
MAX = 100000
MIN = 0
visited = [False] * (MAX + 1)

def bfs(start,end):
  global MAX,MIN,visited

  queue = deque([(start,0)])
  
  visited[start] = True

  timeT = 1e10
  while queue:
    cu,time = queue.popleft()

    if end == cu:
      if time < timeT:
        timeT = time

    if  cu * 2 <= MAX and not visited[cu * 2]:
      visited[cu * 2] = True
      queue.append((cu * 2, time + 1))
    if  cu + 1 <= MAX and not visited[cu + 1]:
      visited[cu + 1] = True
      queue.append((cu + 1, time  + 1))
    if MAX >= cu - 1 >= MIN and not visited[cu - 1]:
      visited[cu - 1] = True
      queue.append((cu - 1, time  + 1))

  return timeT
time = bfs(N,K)

print(time)


    


  