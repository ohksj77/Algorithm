import sys
array = [True for _ in range(2 * 10000 + 1)]
array[0], array[1] = False, False
for i in range(2, int((2 * 10000)**0.5 + 1)):
    if array[i]:
        j = 2
        while i * j <= 2 * 10000:
            array[i * j] = False
            j += 1

num = int(sys.stdin.readline())
for _ in range(num):
    arr_i = []
    arr_j = []
    n = int(sys.stdin.readline())
    A = n // 2
    B = A
    for _ in range(10000):
        if array[A] and array[B]:
            print(A, B)
            break
        A -= 1
        B += 1
