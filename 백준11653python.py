num = int(input())
for i in range(2, num + 1):
    if num == 1:
        break
    while (num / i) % 1 == 0:
        print(i)
        num /= i
