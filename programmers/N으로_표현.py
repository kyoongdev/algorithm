# link : https://school.programmers.co.kr/learn/courses/30/lessons/42895


from collections import deque
from collections import defaultdict
import json


def solution(N, number):
    answer = 0

    numberDict = defaultdict(set)
    resultDict = {}
    if N == number:
        return 1

    for nb in range(1, 10):
        if nb == 1:
            numberDict[nb].add(N)
            resultDict[str(N)] = nb
        else:
            for i in range(1, nb + 1):
                first = str(N) * i
                second = str(N) * (nb - i)
                if i == nb:
                    numberDict[nb].add(int(first))
                    resultDict[first] = nb
                else:
                    for f in numberDict[i]:
                        for s in numberDict[nb - i]:
                            plus = f + s
                            minus = f - s
                            multi = f * s
                            divide = f // s

                            numberDict[nb].add(plus)
                            if minus > 0:
                                if str(minus) in resultDict:
                                    if resultDict[str(minus)] > nb:
                                        resultDict[str(minus)] = nb
                                else:
                                    resultDict[str(minus)] = nb
                                numberDict[nb].add(minus)

                            numberDict[nb].add(multi)

                            if f % s == 0:
                                if str(divide) in resultDict:
                                    if resultDict[str(divide)] > nb:
                                        resultDict[str(divide)] = nb
                                else:
                                    resultDict[str(divide)] = nb
                                numberDict[nb].add(divide)

                            if str(plus) in resultDict:
                                if resultDict[str(plus)] > nb:
                                    resultDict[str(plus)] = nb
                            else:
                                resultDict[str(plus)] = nb

                            if str(multi) in resultDict:
                                if resultDict[str(multi)] > nb:
                                    resultDict[str(multi)] = nb
                            else:
                                resultDict[str(multi)] = nb

    # print(resultDict)
    # print(numberDict)
    if not resultDict.get(str(number)):
        return -1

    return resultDict[str(number)]


"""
N = 5
1개
5

2개
55, 5+5, 5-5, 5*5, 5/5,

3개
555, 
55+5, 55-5, 55*5, 55/5, 


"""




