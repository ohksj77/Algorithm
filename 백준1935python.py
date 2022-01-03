import sys
t = int(sys.stdin.readline())
s = list(sys.stdin.readline().strip())
num = [int(sys.stdin.readline()) for _ in range(t)]
stack = []
def operate(num_2, op ,num_1):
    if op == '+':
        return num_1 + num_2
    elif op == '-':
        return num_1 - num_2
    elif op == '*':
        return num_1 * num_2
    else:
        return num_1 / num_2
for i in s:
    if not i.isalpha():
        a = stack.pop()
        b = stack.pop()
        stack.append(operate(a, i, b))
    else:
        stack.append(num[ord(i) - ord('A')])
print("{:.2f}".format(stack[0]))
