# link :https://school.programmers.co.kr/learn/courses/30/lessons/150369


def solution(cap, n, deliveries, pickups):
    answer = 0
    d_cap, p_cap = 0, 0
    for i in range(n - 1, -1, -1):
        d_cap += deliveries[i]
        p_cap += pickups[i]
        while d_cap > 0 or p_cap > 0:
            d_cap -= cap
            p_cap -= cap
            answer += (i + 1) * 2

    return answer
