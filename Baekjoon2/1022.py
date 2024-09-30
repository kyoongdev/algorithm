r1, c1, r2, c2 = list(map(int, input().split()))


maxLength = 1
arr = []
for x in range(r1, r2 + 1):
    row = []
    for y in range(c1, c2 + 1):
        # print(x, y)
        maxWidth = max(abs(x), abs(y))
        N = maxWidth * 2 + 1
        maxNumb = pow(N, 2)
        cx, cy = x + maxWidth, y + maxWidth
        endX, endY = N - 1, N - 1
        # print("cx, cy :", cx, cy)
        # print("endX, endY :", endX, endY)
        ## 1인 경우
        if cx == 0 and cy == 0 and N == 1:
            row.append(1)
        ##down
        elif cx == endX and 0 < cy < N:
            # print("down")
            numb = maxNumb - (endY - cy)
            length = len(str(numb))
            if length > maxLength:
                maxLength = length

            row.append(numb)
        ##left
        elif cy == 0 and 0 < cx < N:
            # print("left")
            # print("left : ", cx, cy, endX, endY, N, maxNumb)
            numb = maxNumb - (N - 1) - (N - 1 - cx)
            length = len(str(numb))
            if length > maxLength:
                maxLength = length
            row.append(numb)
        ##up
        elif cx == 0 and 0 <= cy < N - 1:

            numb = maxNumb - (N - 1) * 2 - cy
            length = len(str(numb))
            if length > maxLength:
                maxLength = length
            row.append(numb)
        ##right
        elif cy == endY and 0 <= cx < N - 1:
            # print("right")

            numb = maxNumb - (N - 1) * 3 - cx
            # print("numb ", numb, maxNumb, N, cx, cy, endX, endY)
            length = len(str(numb))
            if length > maxLength:
                maxLength = length
            row.append(numb)
    # print(*row)
    arr.append(row)

for row in arr:
    formatted_row = [f"{num:>{maxLength}}" for num in row]
    print(" ".join(formatted_row))


"""

def getShellIndexes(i):
    global N
    ## 아래변
    down = [(N - 1 - i, y) for y in range(N - 1 - i, i, -1)]

    ## 왼쪽변
    left = [(x, i) for x in range(N - 1 - i, i, -1)]

    ## 위쪽변
    up = [(i, y) for y in range(i, N - 1 - i)]

    ## 오른변
    right = [(x, N - 1 - i) for x in range(i, N - 1 - i)]

    return down + left + up + right


arr = [[0] * N for _ in range(N)]
startNumb = pow(N, 2)
mid = maxWidth
arr[mid][mid] = 1

for i in range(maxWidth):
    points = getShellIndexes(i)

    for x, y in points:
        arr[x][y] = startNumb
        startNumb -= 1
"""
