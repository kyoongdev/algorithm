# link : https://school.programmers.co.kr/learn/courses/30/lessons/43165

from itertools import product


def solution(numbers, target):
    answer = 0
    numberLength = len(numbers)

    #     targetPlusMinus = []

    #     for x in product([-1,1] , repeat=len(numbers)):
    #         targetPlusMinus.append(x)

    #     for t in targetPlusMinus:
    #         total = 0
    #         for i,s in enumerate(t):
    #             total += numbers[i] * s
    #         if total == target:
    #             answer += 1
    print("numberLength : ", numberLength)

    def dfs(idx, value):
        nonlocal numbers, target, numberLength, answer

        if idx == numberLength:
            print("result : ", idx, value)
            if value == target:
                answer += 1
            return

        dfs(idx + 1, value + numbers[idx])
        dfs(idx + 1, value - numbers[idx])

    dfs(0, 0)

    return answer
