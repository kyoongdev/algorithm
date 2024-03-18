from collections import deque

T = int(input())
answers = []
for _ in range(T):
  func = input()
  n = int(input())
  arr = input()

  if arr[0] != "[":
    answers.append("error")
    continue
  arr = deque([int(x) for x in arr[1:-1].split(",") if len(x) > 0])

  func = deque([x for x in func])
  isError = False
  isReverse = False
  while func:
    f = func.popleft()
    if f == "R":
      isReverse = not isReverse
    else:

      if len(arr) == 0:
        answers.append("error")
        isError = True
        break
      else:
        if isReverse:
          arr.pop()
        else:
          arr.popleft()
  if not isError:
    if len(arr) == 0:
      answers.append(list(arr))

for a in answers:
  if len(a) == 0:
    print("[]")
  else:
    print(a)


  
