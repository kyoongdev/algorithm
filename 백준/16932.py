
 
from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dxs, dys = [0,0,1,-1],[1,-1,0,0]
dic = dict()

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs(x,y,cnt):
    visited[x][y] = cnt
    que = deque()
    que.append((x,y))
    while que:
        dx,dy = que.popleft()
        for i in range(4):
            nx,ny = dx+dxs[i], dy+dys[i],
            if in_range(nx,ny) and not visited[nx][ny] and graph[nx][ny]:
                visited[nx][ny] = cnt
                que.append((nx,ny))


cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            cnt += 1
            bfs(i,j,cnt)


for i in range(n):
    for j in range(m):
        if visited[i][j] > 0:
            if not visited[i][j] in dic:
                dic[visited[i][j]] = 1
            else:
                dic[visited[i][j]] += 1


answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0: 
            brr= []
            for t in range(4):
                nx,ny = i+dxs[t], j+dys[t]
                if in_range(nx,ny) and visited[nx][ny]:
                    brr.append(visited[nx][ny])
            res = 0
            for k in (set(brr)):
                res += dic[k]
            answer = max(answer,res+1)

print(answer)