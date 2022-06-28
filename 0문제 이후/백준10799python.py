import sys
string = list(sys.stdin.readline().strip())
result = 0
stack = []
for i in range(len(string)):
    if string[i] == '(':
        stack.append(string[i])
    else:
        if string[i - 1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
print(result)
