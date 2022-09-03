import sys
s = list(sys.stdin.readline().rstrip())
t = list(sys.stdin.readline().rstrip())
flag = False
while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if s == t:
        flag = True
        break
sys.stdout.write('1' if flag else '0')
