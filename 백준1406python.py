import sys
w = list(sys.stdin.readline().strip())
stack = []
t = int(sys.stdin.readline())
index = len(w)
for _ in range(t):
    order = sys.stdin.readline().strip()
    if order[0] == 'L' and w:
        stack.append(w.pop())
    elif order[0] == 'D' and stack:
        w.append(stack.pop())
    elif order[0] == 'B' and w:
        w.pop()
    elif order[0] == 'P':
        w.append(order[2])
print("".join(w + list(reversed(stack))))
