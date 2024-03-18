# link : https://school.programmers.co.kr/learn/courses/30/lessons/1845

import math
def solution(nums):
    answer = 0
    pocketMon = {}
    for num in nums:
        if num in pocketMon:
            pocketMon[num] += 1
        else:
            pocketMon[num] = 1
    
    print(len(pocketMon.keys()), len(nums) / 2)
    keysLength = len(pocketMon.keys())
    numsLength = len(nums) / 2
    
    if keysLength <= numsLength:
        return keysLength
    else:
        return numsLength
