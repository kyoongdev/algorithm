# link :https://school.programmers.co.kr/learn/courses/30/lessons/150368


from itertools import product


discounts = [10, 20, 30, 40]


def solution(users, emoticons):
    answer = [0, 0]
    emoticonDiscounts = []

    for cwr in product(discounts, repeat=len(emoticons)):
        emoticonDiscounts.append(list(cwr))

    for discount in emoticonDiscounts:
        emoticonInfos = [
            [emoticons[idx] * (100 - x) / 100, x] for idx, x in enumerate(discount)
        ]
        plusCount = 0
        totalCost = 0
        # print(discount)
        for user in users:
            cost = sum([x[0] for x in emoticonInfos if x[1] >= user[0]])
            # print(cost,user)
            if cost >= user[1]:
                plusCount += 1
            else:
                totalCost += cost
        # if discount[0] == 40:
        #     print("plusCount : ",plusCount, "totalCost : ",totalCost, "answer : ",answer ,plusCount > answer[0])

        if plusCount > answer[0]:
            # print("here",)
            answer = [plusCount, totalCost]
            # print(answer)
        elif plusCount == answer[0]:
            if totalCost > answer[1]:
                answer = [plusCount, totalCost]

    # print(emoticonInfos)

    return answer
