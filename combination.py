def combination(items, maxLength, result, output):
  if len(result) == maxLength:
    output.append(result)
    return
  
  for idx, item in enumerate(items):
    copiedResult = result.copy()
    copiedResult.append(item)
    newItems = items.copy()
    newItems.pop(idx)
    combination(newItems,maxLength, copiedResult, output)
    
output = []
combination([1,2,3,4], 3, [], output)

print(output)
    