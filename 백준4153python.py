import sys
while True:
    a, b, c = map(int,sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break
    a = a**2
    b = b**2
    c = c**2
    if a + b == c or a + c == b or b + c == a:
        print("right")
    else:
        print("wrong")