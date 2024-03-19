# link : https://school.programmers.co.kr/learn/courses/30/lessons/60059


def rotate(nodes):
    width = len(nodes[0])
    newNodes = [[0] * width for _ in range(width)]
    for i in range(width):
        for j in range(width):
            newNodes[j][width - 1 - i] = nodes[i][j]
    return newNodes


def normalize(keys):
    cx, cy = min(keys)

    newKeys = []
    for x, y in keys:
        tmp = []
        for keyX, keyY in keys:
            tmp.append((keyX - x, keyY - y))
        newKeys.append(tmp)

    return newKeys


def keyOrLock(nodes, target):
    result = []
    width = len(nodes[0])
    for x in range(width):
        for y in range(width):
            if nodes[x][y] == target:
                result.append((x, y))
    return result


# def check(keys,locks,lock):
#     width = len(lock)
#     isOk = False
#     for lx,ly in locks:
#         newKeys = []
#         count = 0
#         for x,y in keys:
#             newKeys.append((x+lx,y+ly))
#         for x,y in newKeys:
#             if 0 <= x < width and 0 <= y < width :
#                 if lock[x][y]  == 1:
#                     return False
#                 else:
#                     count += 1
#         if count == len(locks):
#             isOk = True

#     return isOk


def solution(key, lock):
    answer = False

    width = len(lock)
    keyWidth = len(key)

    newLock = [[1] * width * 3 for _ in range(width * 3)]

    def checkMiddle():
        nonlocal width, newLock

        for x in range(width):
            for y in range(width):
                if newLock[x + width][y + width] != 1:
                    return False
        return True

    for x in range(width * width):
        for y in range(width * width):
            if width <= x < width + width and width <= y < width + width:
                newLock[x][y] = lock[x - width][y - width]
    for _ in range(4):
        key = rotate(key)
        for wideX in range(width * 3):
            for wideY in range(width * 3):
                for x in range(keyWidth):
                    for y in range(keyWidth):
                        newLock[wideX + x][wideY + y] += key[x][y]
                if checkMiddle():
                    return True

                for x in range(keyWidth):
                    for y in range(keyWidth):
                        newLock[wideX + x][wideY + y] -= key[x][y]

    return False
