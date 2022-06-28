import sys
expression = list(sys.stdin.readline().strip())
stack = []
temp = ''
for i in expression:
    if i.isalpha():
        temp += i
    else:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                temp += stack.pop()
            stack.pop()
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                temp += stack.pop()
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '/' or stack[-1] == '*'):
                temp += stack.pop()
            stack.append(i)
while stack:
    temp += stack.pop()
print(temp)
