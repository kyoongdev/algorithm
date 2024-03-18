# link : https://school.programmers.co.kr/learn/courses/30/lessons/42746

from functools import cmp_to_key

def sort(a,b):
    
    if a[0] < b[0]:
        return 1
    elif a[0] == b[0]:
        targetA = a + b
        targetB = b + a
        if int(targetA) > int(targetB):
            return -1
        else:
            return 1
    else:
        return -1
    
def solution(numbers):
    answer = ''
    
    strNumbers = list(map(str,numbers))
    sortedNumbers = sorted(strNumbers, key=cmp_to_key(sort))



    return str(int("".join(sortedNumbers)))