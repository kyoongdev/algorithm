import copy

def rotate45(arr,width):
  newArr = copy.deepcopy(arr)


  middle = width // 2
  ## 주 대각선을 가운데 열로 옮긴다
  for i in range(width):
    
    newArr[i][middle] = arr[i][i]
  
  ## 가운데 열을 X의 부 대각선으로 옮긴다
  for i in range(width):
    
    newArr[i][width - 1 - i] = arr[i][middle]

  ## X의 부 대각선을 X의 가운데 행으로 옮긴다
  for i in range(width):
    
    newArr[middle][i] = arr[width - 1 - i][i]

  ## X의 가운데 행을 X의 주 대각선으로 옮긴다
  for i in range(width):

    newArr[i][i] = arr[middle][i]

  return newArr

def rotateMinus45(arr,width):
  newArr = copy.deepcopy(arr)


  middle = width // 2

  ## 주 대각선을 가운데 열로 옮긴다
  for i in range(width):
    
    newArr[middle][i] = arr[i][i]
  
  ## 가운데 열을 X의 부 대각선으로 옮긴다
  for i in range(width):
    
    newArr[i][i] = arr[i][middle]

  ## X의 부 대각선을 X의 가운데 행으로 옮긴다
  for i in range(width):
    newArr[i][middle] = arr[i][width - 1 - i]

  ## X의 가운데 행을 X의 주 대각선으로 옮긴다
  for i in range(width):
    newArr[width - 1 - i][i] = arr[middle][i]

  return newArr


def getDegreeRepeat(d):
  if d == 0:
    return 0
    
  else:
    return abs(d) // 45





T = int(input())
answers = []
for _ in range(T):
  n,d = list(map(int, input().split(" ")))

  numbers = []
  for _ in range(n):
    numbers.append(list(map(int,input().split(" "))))

  repeat = getDegreeRepeat(d)
  for _ in range(repeat):
    if d > 0:
      numbers = rotate45(numbers,n)
    else:
      numbers = rotateMinus45(numbers,n)
  
  answers.append(numbers)

for arr in answers:
  for a in arr:
    print(*a)
