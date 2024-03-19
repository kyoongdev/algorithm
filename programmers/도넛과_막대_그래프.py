# link : https://school.programmers.co.kr/learn/courses/30/lessons/258711


def solution(edges):
    donutCount = 0
    stickCount = 0
    eightCount = 0
    startIndex = 0
    startCount = 0
    edgeDict = {}

    for edge in edges:
        oneKey = str(edge[0])
        twoKey = str(edge[1])
        if twoKey in edgeDict:
            edgeDict[twoKey]["end"] += 1
        else:
            edgeDict[twoKey] = {"end": 1, "start": 0}
        if oneKey in edgeDict:
            edgeDict[oneKey]["start"] += 1
        else:
            edgeDict[oneKey] = {"start": 1, "end": 0}
    for key, value in edgeDict.items():
        if value["start"] >= 2 and value["end"] > 0:
            eightCount += 1
        elif value["start"] >= 2 and value["end"] == 0:
            startIndex = int(key)
            startCount += value["start"]

        elif value["start"] == 0:
            stickCount += 1

    return [startIndex, startCount - (eightCount + stickCount), stickCount, eightCount]
