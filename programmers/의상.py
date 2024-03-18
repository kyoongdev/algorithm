#link : https://school.programmers.co.kr/learn/courses/30/lessons/42578

from itertools import combinations
from functools import reduce

def solution(clothes):
    answer = 1
    combinationCount = 0
    clothDict = {}
    clodict = {}
    
    for cloth in clothes:
        if cloth[1] in clothDict:
            clothDict[cloth[1]] += 1
        else:
            clothDict[cloth[1]]  = 1
    
    for k in clothDict.values():

        answer = (k + 1) * answer
    
                    
    
    return answer -1