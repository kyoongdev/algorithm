# link : https://school.programmers.co.kr/learn/courses/30/lessons/42576


def solution(participant, completion):
    answer = ''
    participantDict ={ }
    
    for i in participant:
        if i in participantDict:
            participantDict[i] += 1
        else:
            participantDict[i] = 1
        
            
    for i in completion:
        if i in participantDict:
            if participantDict[i] == 1:
                del participantDict[i]   
            else:
                participantDict[i] -= 1
    
    for key in participantDict.keys():
        answer = key
    
        
    return answer