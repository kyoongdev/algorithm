import math

N, M, R = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]

outer = min(math.floor(N / 2), math.floor(M / 2))


def rotate_once(i):
    # 껍질의 둘레에 있는 모든 값들 추출
    top = arr[i][i : M - i]
    right = [arr[x][M - i - 1] for x in range(i + 1, N - i - 1)]
    bottom = arr[N - i - 1][i : M - i][::-1]
    left = [arr[x][i] for x in range(i + 1, N - i - 1)][::-1]

    return top + right + bottom + left


def place_once(i, rotated):
    # 껍질에 회전된 값 다시 배치
    idx = 0
    # 윗 변
    for j in range(i, M - i):
        arr[i][j] = rotated[idx]
        idx += 1
    # 오른쪽 변
    for j in range(i + 1, N - i - 1):
        arr[j][M - i - 1] = rotated[idx]
        idx += 1
    # 아래변
    for j in range(M - i - 1, i - 1, -1):
        arr[N - i - 1][j] = rotated[idx]
        idx += 1
    # 왼쪽 변
    for j in range(N - i - 2, i, -1):
        arr[j][i] = rotated[idx]
        idx += 1


def rotate():
    global arr
    for i in range(outer):
        # 현재 껍질에서 회전이 필요한 부분 추출
        shell = rotate_once(i)
        # 실제로는 R % len(shell) 만큼만 회전
        r = R % len(shell)
        rotated_shell = shell[r:] + shell[:r]
        # 회전된 값을 다시 제자리에 배치
        place_once(i, rotated_shell)


rotate()

for row in arr:
    print(*row)
