num = int(input())
count = 1
top = 0
bottom = 0
while num > 0:
    if num - count <= 0:
        if count % 2 == 0:
            bottom = count - num + 1
            top = num
        else:
            bottom = num
            top = count - num + 1
    num -= count
    count += 1
print(top, '/', bottom, sep='')
