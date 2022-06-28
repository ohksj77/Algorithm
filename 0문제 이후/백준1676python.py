import sys
num = int(sys.stdin.readline())
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)
number = factorial(num)
result = 0
for i in list(reversed(str(number))):
    if i == '0':
        result += 1
    else:
        break
print(result)
