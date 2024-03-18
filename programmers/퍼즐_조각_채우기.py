# link :https://school.programmers.co.kr/learn/courses/30/lessons/84021


from collections import deque
from functools import cmp_to_key
from collections import defaultdict

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(game_board, table):
    N = len(game_board)

    tableVisited = set()
    gameVisited = set()

    tableBlocks = []
    gameEmpties = []
    tableDict = defaultdict(list)
    gameDict = defaultdict(list)
    for x in range(N):
        for y in range(N):
            if table[x][y] == 1 and (x, y) not in tableVisited:
                length, visited, blocks = getTableBlocks(table, (x, y), N)
                tableVisited |= visited
                tableDict[length].append(blocks)
            if game_board[x][y] == 0 and (x, y) not in gameVisited:
                length, visited, blocks = getGameEmpty(game_board, (x, y), N)
                gameVisited |= visited
                gameDict[length].append(blocks)

    visited = set()
    count = 0
    for tablelength in tableDict.keys():
        if tablelength in gameDict.keys():

            blocks = tableDict[tablelength]
            empties = gameDict[tablelength]
            for blockIdx in range(len(blocks)):
                for emptyIdx in range(len(empties)):
                    if (tablelength, emptyIdx) in visited:
                        continue
                    else:
                        # isFit = False
                        for i in range(4):
                            # if isFit:
                            # break
                            for j in range(i, 4):
                                if blocks[blockIdx][i] == empties[emptyIdx][j]:
                                    # isFit = True
                                    visited.add((tablelength, emptyIdx))
                                    # print(tablelength)
                                    count += tablelength
                                    break
                        # if isFit:
                        #     break

    return count


def sortTableBlock(a, b):
    if len(a[0]) > len(b[0]):
        return -1
    else:
        return 1


def getGameEmpty(game_board, start, N):
    queue = deque([start])
    idxSet = {start}
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < N
                and (nx, ny) not in idxSet
                and game_board[nx][ny] == 0
            ):
                queue.append((nx, ny))
                idxSet.add((nx, ny))
    rotate90, rotate180, rotate270 = rotate(set(idxSet))
    n_block = normalize(idxSet)
    n_rotate90 = normalize(rotate90)
    n_rotate180 = normalize(rotate180)
    n_rotate270 = normalize(rotate270)

    return len(idxSet), idxSet, [n_block, n_rotate90, n_rotate180, n_rotate270]


def normalize(blocks):
    minX, minY = min(blocks)
    newBlocks = {(x - minX, y - minY) for x, y in blocks}

    return newBlocks


def rotate(block):
    rotate90, rotate180, rotate270 = set(), set(), set()

    while block:
        x, y = block.pop()
        rotate90.add((y, -x))
        rotate180.add((-x, -y))
        rotate270.add((-y, x))

    return rotate90, rotate180, rotate270


def getTableBlocks(table, start, N):
    queue = deque([start])
    idxSet = {start}
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < N
                and (nx, ny) not in idxSet
                and table[nx][ny] == 1
            ):
                queue.append((nx, ny))
                idxSet.add((nx, ny))
    rotate90, rotate180, rotate270 = rotate(set(idxSet))
    n_block = normalize(idxSet)
    n_rotate90 = normalize(rotate90)
    n_rotate180 = normalize(rotate180)
    n_rotate270 = normalize(rotate270)

    return len(idxSet), idxSet, [n_block, n_rotate90, n_rotate180, n_rotate270]
