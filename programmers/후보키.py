# link : https://school.programmers.co.kr/learn/courses/30/lessons/42890

# 유일성 먼저 체크 후 최소성 체크
from itertools import combinations
from collections import defaultdict


def solution(relation):
    answer = 0
    pkCombis = []
    N, M = len(relation), len(relation[0])
    relationIdxes = list(range(M))
    for i in range(1, len(relationIdxes) + 1):
        pkCombis.extend(list(combinations(relationIdxes, i)))

    unique = []
    minLength = 100
    for pkCombi in pkCombis:
        filteredDict = {}
        for x in range(N):
            ft = []
            for y in range(M):
                if y in pkCombi:
                    ft.append(relation[x][y])

            ft = tuple(ft)
            if ft in filteredDict:
                filteredDict[ft] += 1
            else:
                filteredDict[ft] = 1
        # print(filteredDict,pkCombi)
        if len(filteredDict.keys()) == N:
            if len(pkCombi) < minLength:
                minLength = len(pkCombi)

            unique.append(pkCombi)

    tmp = set(unique[:])
    for uIdx in range(len(unique)):
        # if len(u) == minLength:
        #     minimality.append(u)
        #     continue
        for jIdx in range(uIdx + 1, len(unique)):
            if len(set(unique[uIdx]).intersection(unique[jIdx])) == len(unique[uIdx]):
                tmp.discard(unique[jIdx])

    return len(tmp)
