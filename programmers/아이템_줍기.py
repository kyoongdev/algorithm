# link : https://school.programmers.co.kr/learn/courses/30/lessons/87694

from collections import deque
import math


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    possiblePoints = []
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    for x in range(1, 102):
        for y in range(1, 102):
            possiblePoints.append((x, y))
    newRect = []
    for i in rectangle:
        rect = []
        for d in i:
            rect.append(d * 2)
        newRect.append(rect)
    rectangle = newRect

    realPoints = []

    for point in possiblePoints:
        x, y = point
        isInside = False
        outlines = []

        for idx, rect in enumerate(rectangle):
            rectLeftX = rect[0]
            rectLeftY = rect[1]
            rectRightX = rect[2]
            rectRightY = rect[3]
            ## 안에 있는 경우
            if x > rectLeftX and x < rectRightX and y > rectLeftY and y < rectRightY:
                isInside = True
            if (
                (x == rectLeftX and y >= rectLeftY and y <= rectRightY)
                or (y == rectRightY and x >= rectLeftX and x <= rectRightX)
                or (x == rectRightX and y >= rectLeftY and y <= rectRightY)
                or (y == rectLeftY and x >= rectLeftX and x <= rectRightX)
            ):
                outlines.append(idx)
        if not isInside and len(outlines) != 0:
            outlines.sort()
            realPoints.append((x, y))

    visited = [False] * len(realPoints)

    current = [
        [x, y, idx]
        for idx, (x, y) in enumerate(realPoints)
        if x == characterX and y == characterY
    ]

    queue = deque([(characterX, characterY, 0)])

    visited[current[0][-1]] = True

    while queue:
        currentX, currentY, cnt = queue.popleft()
        if currentX == itemX and currentY == itemY:
            answer = cnt

        for idx, (pointX, pointY) in enumerate(realPoints):

            if not visited[idx] and (
                (pointX == currentX and abs(currentY - pointY) == 1)
                or (pointY == currentY and abs(currentX - pointX) == 1)
            ):
                visited[idx] = True
                queue.append((pointX, pointY, cnt + 1))

    return answer / 2
