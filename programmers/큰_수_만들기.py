# link : https://school.programmers.co.kr/learn/courses/30/lessons/42883


def solution(number, k):
    answer = ""

    deletedCount = 0
    stack = []
    for idx, value in enumerate(number):
        if deletedCount == k:
            for value in number[idx:]:
                stack.append(value)
            break
        else:
            if len(stack) == 0:
                stack.append(value)
            else:

                while (
                    deletedCount != k and len(stack) > 0 and int(stack[-1]) < int(value)
                ):
                    stack.pop()
                    deletedCount += 1
                if len(stack) != (len(number) - k):
                    stack.append(value)

    return "".join(stack)
