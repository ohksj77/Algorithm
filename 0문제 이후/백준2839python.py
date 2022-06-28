num = int(input())
result = 0
while num >= 0:
    if num % 5 == 0:
        result += num // 5
        print(result)
        break
    num -= 3
    result += 1
else:
    print(-1)