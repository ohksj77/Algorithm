import sys
t = int(sys.stdin.readline())
stack = []
for _ in range(t):
    order = sys.stdin.readline().split()
    if len(order) == 2:
        stack.append(order[1])
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            top = stack.pop()
            print(top)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
