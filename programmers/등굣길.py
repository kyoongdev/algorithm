# link : https://school.programmers.co.kr/learn/courses/30/lessons/42898


"""
m은 가로 길이
n은 세로 길이

집 좌표 : (1,1)
학교 좌표 : (m,n)
"""
from collections import deque


def solution(m, n, puddles):
    answer = 0
    DIVISION = 1000000007

    home = [0, 0]
    school = (n - 1, m - 1)
    maps = [[0] * m for i in range(n)]

    for puddle in puddles:
        maps[puddle[1] - 1][puddle[0] - 1] = -1
    maps[0][0] = 1
    for y in range(n):
        for x in range(m):
            if x == 0 and y == 0:
                continue
            if maps[y][x] == -1:
                continue
            beforeX = 0 if x - 1 < 0 or maps[y][x - 1] == -1 else maps[y][x - 1]
            beforeY = 0 if y - 1 < 0 or maps[y - 1][x] == -1 else maps[y - 1][x]

            maps[y][x] = beforeX + beforeY

    # for t in maps:
    # print(t)

    return maps[n - 1][m - 1] % DIVISION
