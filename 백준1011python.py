t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    dist = y - x
    count = 0
    move = 1
    distSum = 0
    while distSum < dist:
        count += 1
        distSum += move
        if count % 2 == 0:
            move += 1
    print(count)
