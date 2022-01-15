import sys
m = int(sys.stdin.readline())
v = set()
for _ in range(m):
    op = sys.stdin.readline().rstrip().split()
    if len(op) == 1:
        if op[0] == 'all':
            v = set([i for i in range(1, 21)])
        else:
            v = set()
        continue
    oper, num = op[0], int(op[1])
    if oper == 'add':
        v.add(num)
    elif oper == 'remove':
        v.discard(num)
    elif oper == 'check':
        print(1 if num in v else 0)
    elif oper == 'toggle':
        if num in v:
            v.discard(num)
        else:
            v.add(num)
