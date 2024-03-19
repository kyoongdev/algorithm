# link :https://school.programmers.co.kr/learn/courses/30/lessons/118667


from collections import deque


def solution(queue1, queue2):
    answer = -2
    queue1Sum = sum(queue1)
    queue2Sum = sum(queue2)
    length = len(queue1) * 3 - 3

    if queue1Sum == queue2Sum:
        return 0

    targetNumb = (queue1Sum + queue2Sum) / 2

    if (
        max(queue1) > targetNumb
        or max(queue2) > targetNumb
        or (queue1Sum + queue2Sum) % 2 != 0
    ):
        return -1
    # print(targetNumb,queue1Sum,queue2Sum)
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    result = [0]

    while result[0] <= length:
        if queue1Sum > queue2Sum:
            oneTarget = queue1.popleft()
            queue2.append(oneTarget)
            queue1Sum -= oneTarget
            queue2Sum += oneTarget

            result[0] += 1
        elif queue1Sum < queue2Sum:
            twoTarget = queue2.popleft()
            queue1.append(twoTarget)
            queue1Sum += twoTarget
            queue2Sum -= twoTarget
            result[0] += 1
        else:
            break

    if result[0] > length:
        return -1

    return result[0]


"""
11,12,15,16,19,20,21,22,23,24,30
1,2,4 / 3
2 4 / 3 1
4 / 3 1 2
4 3 / 1 2
3 / 1 2 4
3 1 / 2 4
3 1 2 / 4
1 2 / 4 3

3 5 6 / 2 2
5 6 / 2 2 3
6 / 2 2 3 5
6 2 / 2 3 5

101 100 / 102 103
101 100 102 / 103
100 102 / 103 101
100 102 103 / 101
102 103 / 101 100
103 / 101 100 102
103 101 / 100 102
101 / 100 102 103
101 100 / 102 103


"""
