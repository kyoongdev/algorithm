# link : https://school.programmers.co.kr/learn/courses/30/lessons/258709

from itertools import combinations
from bisect import bisect_left


def solution(dice):
    answer = []
    diceLength = len(dice)
    diceIndexes = [idx for idx in range(diceLength)]
    aSelectedIdx = list(combinations(diceIndexes, diceLength // 2))

    selections = []

    winLooseDict = {}
    for aIdxes in aSelectedIdx:
        bIdxes = tuple(set(diceIndexes) - set(aIdxes))
        winLooseDict[aIdxes] = {"WIN": 0}

        selections.append((aIdxes, bIdxes))

    def selectNumbers(dices, startIndex, result, output):
        nonlocal diceLength
        if len(result) == diceLength // 2:
            output.append(sum(result))
            return

        for d in dices[startIndex]:
            selectNumbers(dices, startIndex + 1, [*result, d], output)

    maxCount = 0
    answerDict = {}
    for select in selections:
        a, b = select
        aDices = []
        bDices = []
        for ai in a:
            aDices.append(dice[ai])
        for bi in b:
            bDices.append(dice[bi])
        aResult = []
        selectNumbers(aDices, 0, [], aResult)
        aResult.sort()
        bResult = []
        selectNumbers(bDices, 0, [], bResult)
        bResult.sort()
        answerDict[a] = (aResult, bResult)

    for key in answerDict:
        aResult, bResult = answerDict[key]

        count = 0
        for ar in aResult:
            idx = bisect_left(bResult, ar)
            count += idx
        if maxCount < count:
            maxCount = count
            answer = key

    return [int(x) + 1 for x in answer]
