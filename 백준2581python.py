min_num = int(input())
max_num = int(input())
array = []
for i in range(min_num, max_num + 1):
    count = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                count += 1
            if count > 0:
                break
        if count == 0:
            array.append(i)
if len(array) == 0:
    print(-1)
else:
    print(sum(array))
    print(min(array))
