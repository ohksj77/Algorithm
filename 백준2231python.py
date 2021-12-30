import sys
n = int(sys.stdin.readline())
num = 1
flag = 0
for _ in range(n):
    temp = 0
    num = str(num)
    for j in range(len(num)):
        temp += int(num[j])
    num = int(num)
    temp += num
    if temp == n:
        flag += 1
        break
    num += 1
if flag == 0:
    print(0)
else:
    print(num)
