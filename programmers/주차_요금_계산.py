# link :https://school.programmers.co.kr/learn/courses/30/lessons/92341
import math


def solution(fees, records):
    answer = []
    cars = set()
    carsDict = {}
    maxTime = 23 * 60 + 59
    for r in records:
        values = r.split(" ")
        cars.add(values[1])
        times = values[0].split(":")
        if values[1] not in carsDict:
            carsDict[values[1]] = {"IN": [], "OUT": []}
        carsDict[values[1]][values[2]].append(int(times[0]) * 60 + int(times[1]))

    carsList = list(cars)
    carsList.sort()

    for car in carsList:
        ins = carsDict[car]["IN"]
        outs = carsDict[car]["OUT"]
        if len(ins) != len(outs):
            outs.append(maxTime)
        parkingTime = 0
        for idx, t in enumerate(ins):
            parkingTime += outs[idx] - t
        money = fees[1]
        if parkingTime > fees[0]:
            money += math.ceil((parkingTime - fees[0]) / fees[2]) * fees[3]

        answer.append(money)

    return answer
