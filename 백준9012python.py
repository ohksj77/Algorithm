import sys
t = int(sys.stdin.readline())
for _ in range(t):
    string = sys.stdin.readline().strip()
    stack = []
    flag = False
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(string[i])
        else:
            if not stack:
                flag = True
            else:
                stack.pop()
    if not flag and not stack:
        print('YES')
    else:
        print('NO')
