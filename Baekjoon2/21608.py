N = int(input())

students = []
studentLike = dict(list())
for _ in range(pow(N, 2)):
    student = list(map(int, input().split()))
    students.append(student)
    studentLike[student[0]] = student[1:]


classRooms = [[0] * N for _ in range(N)]


classRooms[1][1] = students[0][0]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def search(likeList):

    global classRooms

    maxCount = 0
    targets = []
    for x in range(N):
        for y in range(N):
            if classRooms[x][y] == 0:
                tmpCount = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < N and 0 <= ny < N and classRooms[nx][ny] in likeList:
                        tmpCount += 1
                if tmpCount > maxCount:
                    targets = [(x, y)]
                    maxCount = tmpCount
                elif tmpCount == maxCount:
                    targets.append((x, y))
    if len(targets) == 0:
        for x in range(N):
            for y in range(N):
                if classRooms[x][y] == 0:
                    targets.append((x, y))

        if len(targets) == 1:
            return targets[0]
    vacantSeatCount = 0
    vacantTargets = []
    for tx, ty in targets:

        tmpCount = 0

        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if 0 <= nx < N and 0 <= ny < N and classRooms[nx][ny] == 0:
                # print(nx, ny)
                tmpCount += 1

        if tmpCount > vacantSeatCount:
            vacantTargets = [(tx, ty)]
            vacantSeatCount = tmpCount
        elif tmpCount == vacantSeatCount:
            vacantTargets.append((tx, ty))

    vacantTargets.sort()

    return vacantTargets[0]


for stu in students[1:]:

    x, y = search(stu[1:])

    classRooms[x][y] = stu[0]

score = [0, 1, 10, 100, 1000]
answer = 0

for x in range(N):
    for y in range(N):

        likeCount = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < N
                and classRooms[nx][ny] in studentLike[classRooms[x][y]]
            ):
                likeCount += 1

        answer += score[likeCount]


print(answer)
