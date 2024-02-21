def permutation(items, maxLength, result, output):
  if len(result) == maxLength:
    output.append(result)
    return
  
  for item in items:
    copiedResult = result.copy()
    copiedResult.append(item)
    permutation(items, maxLength, copiedResult, output)

output = []
permutation([1,2,3,4], 3, [],output)

print(output)