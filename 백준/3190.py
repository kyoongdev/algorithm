from collections import deque

N = int(input())
K = int(input())

apples = []

for _ in range(K):
    apples.append(list(map(int, input().split())))

L = int(input())

snakes = {}
for _ in range(L):
    time, direction = input().split()
    snakes[time] = direction


board = [[0] * N for _ in range(N)]

for apple in apples:
    x, y = apple
    board[x - 1][y - 1] = 1


queue = deque([(0, 0)])
time = 0
tails = deque([(0, 0)])
rotate = 0
rotation = {
    "0": (0, 1),
    "90": (1, 0),
    "180": (0, -1),
    "270": (-1, 0),
}
visits = [[0] * N for _ in range(N)]
visits[0][0] = 1

while queue:

    x, y = queue.popleft()
    # print("head", x, y)
    # board[x][y] = 2
    if snakes.get(str(time)):
        # print(snakes[str(time)])
        if snakes[str(time)] == "D":
            if rotate == 270:
                rotate = 0
            else:
                rotate += 90

        else:
            if rotate == 0:
                rotate = 270
            else:
                rotate -= 90
        dx, dy = rotation[str(rotate)]
        x += dx
        y += dy
    else:
        dx, dy = rotation[str(rotate)]
        x += dx
        y += dy

    if x < 0 or x >= N or y < 0 or y >= N or (x, y) in tails:
        time += 1
        break
    time += 1
    visits[x][y] += 1
    if board[x][y] == 1:
        board[x][y] = 0
        queue.append((x, y))
        tails.append((x, y))
    else:
        # print("tail", tails)
        tails.popleft()
        tails.append((x, y))
        queue.append((x, y))
    # print("time : ", time)
    # for b in board:
    # print(*b)

    # print("----")
count = 0
for v in visits:
    for t in v:
        count += t
print(count)
