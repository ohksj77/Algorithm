import sys
while True:
    sentence = sys.stdin.readline().rstrip('\n')
    small, big, num, space = 0, 0, 0, 0
    if not sentence:
        break
    for i in sentence:
        if i.islower():
            small += 1
        elif i.isupper():
            big += 1
        elif i.isdigit():
            num += 1
        elif i.isspace():
            space += 1
    print(small, big, num, space)
