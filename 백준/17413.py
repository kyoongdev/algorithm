from collections import deque
S = input()

tagOpenCount = 0
tagCloseCount = 0
reverseWords = []
reverseStartIdx = -1
isTagEnd = True


strList = [x for x in S+" "]
for idx,s in enumerate(strList):
  # print(s)
  if s == " " and isTagEnd and  reverseStartIdx  != -1:

    reverseWords.append((reverseStartIdx,idx))
    reverseStartIdx = -1
  elif s != "<" and s != ">"  and isTagEnd and reverseStartIdx == -1:
    reverseStartIdx = idx
  elif s == "<":
    # print("tagOpenCount",tagOpenCount)
    if   reverseStartIdx  != -1:
      reverseWords.append((reverseStartIdx,idx))
      reverseStartIdx = -1
    
    isTagEnd = False
    tagOpenCount += 1

  elif s == ">":
    isTagEnd = True 
    tagCloseCount += 1
    if tagOpenCount == tagCloseCount  == 2:
      tagCloseCount = 0
      tagOpenCount = 0


# print(reverseWords)
for rw in reverseWords:
  start,end = rw

  target =[*strList[start:end]]
  target.reverse()
  target = deque(target)
  for i in range(start,end):
    strList[i] = target.popleft()


print("".join(strList[:-1]))