# link : https://school.programmers.co.kr/learn/courses/30/lessons/77486

import math

COST = 100


def solution(enroll, referral, seller, amount):
    answer = []

    enrollDict = {}
    amountDict = {}
    for i in range(len(enroll)):
        enrollDict[enroll[i]] = referral[i]
        amountDict[enroll[i]] = 0

    for i in range(len(seller)):

        current = seller[i]
        cash = amount[i] * 100
        amountDict[current] += amount[i] * 100
        while enrollDict[current] != "-" and cash != 0:
            # if cash == 0:
            #     break
            cash = int(0.1 * cash)
            amountDict[current] -= cash
            amountDict[enrollDict[current]] += cash
            current = enrollDict[current]

        if enrollDict[current] == "-":
            amountDict[current] -= int(cash * 0.1)

        # print(i,current,cash)
    for e in enroll:
        answer.append(math.ceil(amountDict[e]))

    return answer
