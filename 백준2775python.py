t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    if n == 1:
        print(1)
    else:
        result = 1
        for i in range(1, k + 2):
            result = (result * n) // i
            n += 1
        print(result)
