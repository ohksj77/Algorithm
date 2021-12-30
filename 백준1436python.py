import sys
n = int(sys.stdin.readline())
count = 0
six = 666
while True:
    if '666' in str(six):
        count += 1
    if count == n:
        print(six)
        break
    six += 1
