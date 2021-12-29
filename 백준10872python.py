import sys
n = int(sys.stdin.readline())
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)
if n == 0:
    print(1)
else:
    print(factorial(n))
