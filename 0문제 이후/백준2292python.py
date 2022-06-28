num = int(input())
count = 1
temp = 6
result = 1
while num > count:
    result += 1
    count += temp
    temp += 6
print(result)
