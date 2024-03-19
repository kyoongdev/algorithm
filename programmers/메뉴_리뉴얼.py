# link : https://school.programmers.co.kr/learn/courses/30/lessons/72411

import itertools


def solution(orders, course):
    answer = set()
    orderDict = {}
    maxLength = 0
    for order in orders:
        orderLength = len(order)
        splittedOrder = [o for o in order]
        for i in course:
            combinations = list(itertools.combinations(splittedOrder, i))

            for c in combinations:
                cList = list(c)
                cList.sort()
                key = "".join(cList)

                if key in orderDict:
                    orderDict[key] += 1
                else:
                    orderDict[key] = 1

    for c in course:
        keys = [key for key in orderDict.keys() if len(key) == c]
        maxCount = 0
        tmpAnswers = []
        for key in keys:

            if orderDict[key] < 2:
                continue

            if maxCount < orderDict[key]:
                tmpAnswers.clear()
                tmpAnswers.append(key)
                maxCount = orderDict[key]
            elif maxCount == orderDict[key]:
                tmpAnswers.append(key)

        for t in tmpAnswers:
            answer.add(t)

    result = list(answer)
    result.sort()
    return result
