# link : https://school.programmers.co.kr/learn/courses/30/lessons/42839
import math


def getCombi(numbers, maxLength, output, result):
    if len(result) == maxLength:

        return output.append(int("".join(result)))

    for idx, number in enumerate(numbers):
        copiedNumbers = numbers.copy()
        copiedNumbers.pop(idx)
        copiedResult = result.copy()
        copiedResult.append(number)
        getCombi(copiedNumbers, maxLength, output, copiedResult)


def checkPrime(number):
    if number == 1 or number == 0:
        return False
    if number == 2:
        return True
    count = 0

    for i in range(2, math.ceil(math.sqrt(number)) + 1):

        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    splittedNumbers = [n for n in numbers]

    result = []

    for i in range(len(numbers)):
        output = []
        getCombi(splittedNumbers, i + 1, output, [])
        result = [*result, *output]

    for value in set(result):
        if checkPrime(value):

            answer += 1

    return answer
