target = input()


acc = 0
tmpAcc = 1
stack = []


for tIdx, t in enumerate(target):

    if t == "(":
        tmpAcc *= 2
        stack.append(t)
    elif t == "[":
        tmpAcc *= 3
        stack.append(t)
    elif t == "]":

        if not stack or stack[-1] != "[":
            acc = 0
            break

        if target[tIdx - 1] == "[":
            acc += tmpAcc

        tmpAcc //= 3
        stack.pop()
    elif t == ")":
        if not stack or stack[-1] != "(":
            acc = 0
            break
        if target[tIdx - 1] == "(":
            acc += tmpAcc
        tmpAcc //= 2
        stack.pop()

if len(stack) != 0:
    print(0)
else:
    print(acc)
