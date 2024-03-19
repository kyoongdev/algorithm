# link : https://school.programmers.co.kr/learn/courses/30/lessons/64064


from collections import deque


def solution(user_id, banned_id):
    answer = 0
    counts = []
    result = []
    for idx, banned in enumerate(banned_id):
        count = 0
        baseUnBlockCount = len([x for x in banned if x != "*"])
        tmpResult = []
        for user in [u for u in user_id if len(u) == len(banned)]:
            correctCount = 0

            for b, u in zip(banned, user):
                if b != "*" and b == u:

                    correctCount += 1
            if correctCount == baseUnBlockCount:
                tmpResult.append(user)
        result.append(tmpResult)

    def search(items, tmpResult, output):
        nonlocal banned_id
        if len(tmpResult) == len(banned_id):
            tmpResult.sort()
            if tmpResult not in output:
                output.append(tmpResult)
            return

        for idx, item in enumerate(items):
            for i in item:
                if i not in tmpResult:
                    search(items[idx + 1 :], [*tmpResult, i], output)

    output = []
    search(result, [], output)
    # print(output)

    return len(output)
