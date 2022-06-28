n = int(input())
array = list(map(int, input().split()))
sum = 0
for i in range(n):
    count = 0
    for j in range(2, array[i]):
        if array[i] == 1:
            break
        if array[i] % j == 0:
            count += 1
    if count == 0 and array[i] != 1:
        sum += 1
print(sum)
