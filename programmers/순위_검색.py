# link : https://school.programmers.co.kr/learn/courses/30/lessons/72412


from bisect import bisect_left
import itertools


def solution(info, query):
    answer = []
    infoLists = [i.split(" ") for i in info]
    queryLists = [i.replace(" and", "").split(" ") for i in query]

    scoreDict = {}
    for inf in infoLists:
        for t in itertools.product(*[["-", x] for x in inf[:-1]]):
            if t in scoreDict:
                scoreDict[t].append(int(inf[-1]))
            else:
                scoreDict[t] = [int(inf[-1])]
    for s in scoreDict:
        scoreDict[s].sort()

    for q in queryLists:
        joined = tuple(q[:-1])
        score = int(q[-1])
        if joined not in scoreDict or len(scoreDict[joined]) == 0:
            answer.append(0)
        else:
            answer.append(
                len(scoreDict[joined]) - bisect_left(scoreDict[joined], score)
            )

    return answer
