import sys
x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())
x3, y3 = map(int, sys.stdin.readline().split())
result_x, result_y = 0, 0
for _ in range(3):
    if x1 == x2:
        result_x = x3
    elif x1 == x3:
        result_x = x2
    else:
        result_x = x1
    if y1 == y2:
        result_y = y3
    elif y1 == y3:
        result_y = y2
    else:
        result_y = y1
print(result_x,result_y)