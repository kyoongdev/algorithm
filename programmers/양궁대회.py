# link : https://school.programmers.co.kr/learn/courses/30/lessons/92342

import itertools


def solution(n, info):
    answer = []
    targets = [x for x in range(11)]
    winInfo = []
    maxScore = 0
    for i in range(1, n + 1):
        wins = list([list(x) for x in itertools.combinations(targets, i)])
        for win in wins:
            winInfo.append(win)

    for w in winInfo:
        lion = [0] * 11
        lionScore = 0
        apeachScore = 0
        for idx in w:
            lion[idx] = info[idx] + 1
        if sum(lion) > n:
            continue

        for idx, l in enumerate(lion):
            if l > info[idx]:
                lionScore += 10 - idx
            elif info[idx] != 0 and l <= info[idx]:
                apeachScore += 10 - idx
        if lionScore == apeachScore:
            continue
        if maxScore < lionScore - apeachScore:
            answer.clear()
            answer.append(lion)
            maxScore = lionScore - apeachScore
        elif maxScore == lionScore - apeachScore:
            answer.append(lion)

    for idx, a in enumerate(answer):
        sumA = sum(a)
        if sumA == n:
            continue
        for i in range(10, -1, -1):
            sumA = sum(a)
            if info[i] == 0:
                continue
            if sumA + info[i] - 1 == n:
                a[i] = info[i] - 1
            elif sumA + info[i] - 1 > n:
                current = 1
                while True:
                    current += 1
                    if sumA + info[i] - current == n:
                        print(info[i] - current)
                        a[i] = info[i] - current
                        break
                break

    if len(answer) == 0:
        return [-1]

    answer.sort()
    minScore = 0

    for idx, l in enumerate(answer[0]):
        minScore += (10 - idx) * l
    realAnswer = answer[0]
    for a in answer[1:]:
        score = 0
        for idx, l in enumerate(a):
            score += (10 - idx) * l
        if score <= minScore:
            realAnswer = a
            minScore = sum(a)
    return realAnswer
