from collections import deque
import math

N = input()
M = int(input())
wrongs = input().split(" ") if M > 0 else []
current = 100
if int(N) == 100:
  print(0)
  exit()

# if M == 0:
#   print(abs(len(N) - 100))
#   exit()
  
defaultNumbers = set([n for n in range(10)])
wrongs = set([int(n) for n in wrongs])

restNumbers = defaultNumbers - wrongs
restNumbers = list(restNumbers)
lenRest = len(restNumbers)
visited = [[False] * lenRest for _ in range(len(N))]
restNumbers = [(restNumbers,i) for i in range(len(N))]

output = []

restNumberQueue = deque(restNumbers)
while restNumberQueue:

  restNumber,idx = restNumberQueue.popleft()
  minDiff = int(N)
  number = 0
  for i in restNumber:
    tmpOutput= [*output,i]
    currentNumber =  int("".join([str(o) for o in tmpOutput])) * math.pow(10, len(N) - len(tmpOutput))
    diff = abs(int(N) - currentNumber) 
    print([*output,i], currentNumber,diff)
    if diff < minDiff:
      minDiff = diff
      number = i
  
  output.append(number)



resultNumber = int("".join([str(o) for o in output]))
diff = abs(int(N) - resultNumber)
print("output",output)
print(diff + len(N) if abs(int(N) - 100) > diff + len(N) else abs(int(N) - 100))
# current = 0
# isOver = False
# def dfs(result):
#   global current,output,isOver
#   print("result : ", result, len(result), len(N))
#   if len(result) == len(N):
#     output = result.copy()
#     isOver= True
#     return
  
#   for rnIdx in range(len(restNumbers[current]) - 1, -1, -1):
#     tmpResult = [*result, str(restNumbers[current][rnIdx])]
    
#     if not isOver and int(N) >= int("".join(tmpResult)) * math.pow(10, len(N) - len(tmpResult))  and not visited[current][rnIdx]:
#       print("처음 :  ",int("".join(tmpResult)) * math.pow(10, len(N) - len(tmpResult)),result)
#       visited[current][rnIdx] = True
#       result.append(str(restNumbers[current][rnIdx]))
#       current += 1
#       dfs(result)
#       result.pop()
#       current -= 1
    

      
# dfs([])
    
    
# print(output)
# outputNumber= int("".join(output))
# print(int(N)-outputNumber)
  


  
  
  
  