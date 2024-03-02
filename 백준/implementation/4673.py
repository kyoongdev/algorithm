numbers = [0] * 10000

for i in range(1,10001):
  targetNumber= str(i)
  initNumber = i
  for v in targetNumber:
    initNumber += int(v)
  if initNumber < 10000:
    numbers[initNumber] = initNumber
    
  
for idx,n in enumerate(numbers):
  if n == 0 and idx != 0:
    print(idx )
  

  
  