T = int(input())
orders = []
for i in range(T):
    orders.append(input())

"""
F : 앞으로
B : 뒤로
L : 왼쪽 회전
R : 오른쪽 회줜
"""

heading = [[-1, 0], [0, -1], [1, 0], [0, 1]]
currentHeading = 0


def getHeading(order):
    global currentHeading
    if order == "L":
        if currentHeading == 3:
            currentHeading = 0
        else:
            currentHeading += 1
    elif order == "R":

        if currentHeading == 0:
            currentHeading = 3
        else:
            currentHeading -= 1


def getNext(order, location):
    global currentHeading
    cx, cy = location
    if order == "F" or order == "B":
        if order == "F":
            return (cx + heading[currentHeading][0], cy + heading[currentHeading][1])

        else:
            return (cx - heading[currentHeading][0], cy - heading[currentHeading][1])
    else:
        getHeading(order)
        return location


for order in orders:
    currentHeading = 0
    arr = [[0] * 10 for j in range(10)]
    currentLocation = (0, 0)
    locations = set()
    locations.add(currentLocation)
    for o in order:

        nx, ny = getNext(o, currentLocation)

        currentLocation = (nx, ny)
        locations.add(currentLocation)

    locations = list(locations)
    locations.sort()

    fx, fy = locations[0]

    locations[0] = (0, 0)

    for i in range(1, len(locations)):
        lx, ly = locations[i]
        locations[i] = (lx - fx, ly - fy)
    # print(locations)
    minX = float("inf")
    minY = float("inf")
    maxX = 0
    maxY = 0

    for lx, ly in locations:
        if lx < minX:
            minX = lx
        if ly < minY:
            minY = ly
        if lx > maxX:
            maxX = lx
        if ly > maxY:
            maxY = ly
    # print(minX, minY, maxX, maxY)
    area = (maxX - minX) * (maxY - minY)
    print(area)
