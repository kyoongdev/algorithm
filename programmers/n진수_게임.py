# link : https://school.programmers.co.kr/learn/courses/30/lessons/17687


def solution(n, t, m, p):
    answer = "0"
    notation = "0123456789ABCDEF"

    for num in range(1, m * t):
        result = ""
        while num > 0:
            # print(num)
            num, remainder = divmod(num, n)
            # print(num,remainder)
            result += notation[remainder]

        answer += result[::-1]
    # print(answer[p-1::m])
    return answer[p - 1 :: m][:t]


"""


1 3 5
3번째 3 6 
"""
