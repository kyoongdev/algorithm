# link : https://school.programmers.co.kr/learn/courses/30/lessons/258707

from collections import deque
from itertools import combinations


def solution(coin, cards):
    answer = 1

    n = len(cards)
    discard = n + 1

    take = cards[: n // 3]
    cards = deque(cards[n // 3 :])
    possible = []

    def update_possible():
        if cards:
            possible.append(cards.popleft())
            possible.append(cards.popleft())

    def check(candidateOne, candidateTwo):

        for c in list(candidateOne):
            if n + 1 - c in candidateTwo:
                candidateOne.remove(c)
                candidateTwo.remove(n + 1 - c)
                return True
        return False

    while cards:
        update_possible()

        if check(take, take):
            answer += 1
        elif coin >= 1 and check(take, possible):
            coin -= 1
            answer += 1
        elif coin >= 2 and check(possible, possible):
            coin -= 2
            answer += 1
        else:
            break

    return answer
