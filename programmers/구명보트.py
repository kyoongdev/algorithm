# link : https://school.programmers.co.kr/learn/courses/30/lessons/42885

# 한번에 최대 2명 / 무게 제한
# 구명보트 최대한 적게 사용
import math


def solution(people, limit):

    people.sort(reverse=True)
    boatCount = 0
    boats = []
    peopleLength = len(people)
    for idx, person in enumerate(people):
        if peopleLength == idx + 1:
            boats.append([person])
            break

        lastPerson = people[-1]

        if lastPerson + person <= limit:
            people.pop()
            boats.append([person, lastPerson])
        else:
            boats.append([person])

    return len(boats)
