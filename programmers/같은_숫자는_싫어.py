# link : https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []

    for value in arr:
        
        if len(answer) > 0 and value != answer[-1]:
            
            answer.append(value)
        elif len(answer) == 0:
            answer.append(value)
    return answer