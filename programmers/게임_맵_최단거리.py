# link : https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque


def solution(maps):
    m = len(maps)
    n = len(maps[0])
    startPoint = [0, 0]
    queue = deque([startPoint])

    xPoint = [0, 0, -1, 1]
    yPoint = [-1, 1, 0, 0]

    while queue:
        current = queue.popleft()
        for i in range(0, 4):
            nextX = current[0] + xPoint[i]
            nextY = current[1] + yPoint[i]
            if 0 <= nextX <= m - 1 and 0 <= nextY <= n - 1 and maps[nextX][nextY] == 1:
                queue.append([nextX, nextY])
                maps[nextX][nextY] = maps[current[0]][current[1]] + 1

    if maps[m - 1][n - 1] == 1:
        return -1
    else:
        return maps[m - 1][n - 1]
