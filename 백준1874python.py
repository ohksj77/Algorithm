import sys
t = int(sys.stdin.readline())
num_arr = []
op_arr = []
count = 0
flag = True
for _ in range(t):
    n = int(sys.stdin.readline())
    while count < n:
        count += 1
        num_arr.append(count)
        op_arr.append('+')
    if num_arr[-1] == n:
        num_arr.pop()
        op_arr.append('-')
    else:
        flag = False
if flag is False:
    print('nO')
else:
    print("\n".join(op_arr))
