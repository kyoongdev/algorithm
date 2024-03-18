# link : https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    phoneDict = {}
    phone_book.sort()
    for phone in phone_book:
        for idx in range(len(phone)):
            if phone[0:idx+1] in phoneDict:
                answer = False
        phoneDict[phone] = True
    
    return answer