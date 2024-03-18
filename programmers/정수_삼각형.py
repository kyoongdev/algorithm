# link : https://school.programmers.co.kr/learn/courses/30/lessons/43105


def solution(triangle):
    answer = triangle[0][0]
    memoization = [[triangle[0][0]]]
    for tIdx, t in enumerate(triangle):
        memo = []
        # print(t)
        if tIdx == 0:
            continue
        for nIdx, n in enumerate(t):
            ## 왼쪽 / 가운데 / 맨 끝 경우
            ## 맨끝
            # print(nIdx,n)
            if len(t) - 1 == nIdx:
                v1 = memoization[tIdx - 1][nIdx - 1] + n
                if v1 > answer:
                    answer = v1
                memo.append(v1)
            elif nIdx == 0:
                v1 = memoization[tIdx - 1][0] + n

                if v1 > answer:
                    answer = v1
                memo.append(v1)
            else:
                v1 = memoization[tIdx - 1][nIdx - 1] + n
                v2 = memoization[tIdx - 1][nIdx] + n
                maxValue = max(v1, v2)
                if maxValue > answer:
                    answer = maxValue
                memo.append(maxValue)
        memoization.append(memo)

    return answer
