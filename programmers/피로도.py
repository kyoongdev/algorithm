# link : https://school.programmers.co.kr/learn/courses/30/lessons/87946


def solution(k, dungeons):
    answer = 0
    output = []
    getCombination(dungeons, [], output)

    for dungeon in output:
        piro = k
        count = 0
        for dungeonDetail in dungeon:
            if piro >= dungeonDetail[0]:
                count += 1
                piro -= dungeonDetail[1]
        if count > answer:
            answer = count

    return answer


def getCombination(dungeons, result, output):

    if len(dungeons) == 0:
        return output.append(result)

    else:
        for idx, dungeon in enumerate(dungeons):
            newDungeons = dungeons.copy()
            newDungeons.pop(idx)

            newResult = result.copy()
            newResult.append(dungeons[idx])

            getCombination(newDungeons, newResult, output)
