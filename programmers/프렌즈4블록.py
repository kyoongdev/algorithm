# link : https://school.programmers.co.kr/learn/courses/30/lessons/17679


def solution(m, n, board):
    answer = 0

    board = [list(b) for b in board]
    for b in board:
        print(b)

    def check(x, y):
        nonlocal board, m, n
        b = board[x][y]

        if x + 1 >= m or y + 1 >= n:
            return False

        if b != "0":
            if (
                b == board[x + 1][y]
                and b == board[x][y + 1]
                and b == board[x + 1][y + 1]
            ):
                return True

    while True:

        checked = []
        for x in range(m):
            for y in range(n):
                isExists = check(x, y)
                if isExists:
                    checked.append((x, y))
                    checked.append((x + 1, y))
                    checked.append((x, y + 1))
                    checked.append((x + 1, y + 1))

        if len(checked) == 0:
            break

        for x, y in checked:
            board[x][y] = "0"

        for x in range(m - 1, -1, -1):
            for y in range(n):
                zeros(x, y, board)

    for x in range(m):
        for y in range(n):
            if board[x][y] == "0":
                answer += 1

    # for b in board:
    #     print(b)

    return answer


def zeros(x, y, b):
    if b[x][y] == "0":
        for i in range(x - 1, -1, -1):
            if b[i][y] != "0":
                b[x][y], b[i][y] = b[i][y], b[x][y]
                break
