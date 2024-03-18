# link : https://school.programmers.co.kr/learn/courses/30/lessons/42862


def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    lostCopy = lost.copy()
    reserveCopy = reserve.copy()
    lost = [x for x in lost if x not in reserveCopy]
    reserve = [x for x in reserve if x not in lostCopy]

    lostPeopleLength = len(lost)

    for lostPeople in lost:

        matches = [x for x in reserve if x == lostPeople - 1 or x == lostPeople + 1]

        if len(matches) > 0:
            minValue = min(matches)
            reserve.remove(minValue)
            lostPeopleLength -= 1

    return n - lostPeopleLength
