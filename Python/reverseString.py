input = "hello this is shiva and how are you doing"

stack = list(input)
reverseList = []
for i in range(0, len(input)):
    reverseList.append(stack.pop(-1))

print(''.join(reverseList))
