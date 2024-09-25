# link :https://school.programmers.co.kr/learn/courses/30/lessons/92344


"""
파괴된 순간에 복구 가능
내구도 음수 가능

"""


def solution(board, skill):
    answer = 0

    X = len(board)
    Y = len(board[0])
    initBoard = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for s in skill:
        skillType, startX, startY, endX, endY, degree = s

        if skillType == 1:
            initBoard[startX][startY] -= degree
            initBoard[startX][endY + 1] += degree
            initBoard[endX + 1][startY] += degree
            initBoard[endX + 1][endY + 1] -= degree
        else:
            initBoard[startX][startY] += degree
            initBoard[startX][endY + 1] -= degree
            initBoard[endX + 1][startY] -= degree
            initBoard[endX + 1][endY + 1] += degree

    # for b in initBoard:
    #     print(b)

    for x in range(1, X + 1):
        for y in range(Y + 1):
            initBoard[x][y] += initBoard[x - 1][y]

    for x in range(X + 1):
        for y in range(1, Y + 1):
            initBoard[x][y] += initBoard[x][y - 1]

    for x in range(X):
        for y in range(Y):
            if board[x][y] + initBoard[x][y] > 0:
                answer += 1

    return answer



