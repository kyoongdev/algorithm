# link :https://school.programmers.co.kr/learn/courses/30/lessons/42747


def solution(citations):
    answer = 0
    citations.sort()

    for idx, citation in enumerate(citations):
        restLength = len(citations[idx:])
        h = 0

        if restLength > citation:
            h = citation
        else:
            h = restLength
        if answer < h:
            answer = h

    return answer
