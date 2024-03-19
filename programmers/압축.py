# link : https://school.programmers.co.kr/learn/courses/30/lessons/17684
import string
from collections import deque


def test(msg):
    answer = []
    alphas = string.ascii_uppercase
    dictionary = {}
    for idx, alpha in enumerate(alphas):
        dictionary[alpha] = idx + 1

    msgQeue = deque([m for m in msg])

    current = 27
    alpha = msgQeue.popleft()

    while msgQeue:
        nextAlpha = msgQeue.popleft()
        # print(msgQeue)
        if dictionary.get(alpha) and not dictionary.get(alpha + nextAlpha):
            # print(alpha,nextAlpha,answer)
            answer.append(dictionary[alpha])
            dictionary[alpha + nextAlpha] = current
            current += 1
            alpha = nextAlpha
        elif dictionary.get(alpha + nextAlpha):
            alpha = alpha + nextAlpha
    answer.append(dictionary[alpha])
    return answer


def solution(msg):

    return test(msg)
