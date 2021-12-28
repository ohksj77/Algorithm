import sys
array1 = [True for _ in range(2 * 123456 + 1)]
array1[0], array1[1] = False, False
for i in range(2, int((2 * 123456)**0.5 + 1)):
    if array1[i]:
        j = 2
        while i * j <= 2 * 123456:
            array1[i * j] = False
            j += 1

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if array1[i]:
            count += 1
    print(count)
