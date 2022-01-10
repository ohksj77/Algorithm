import sys
n = sys.stdin.readline().rstrip()
length = len(n) - 1
result = 0
i = 0
while i < length:
    result += 9 * (10 ** i) * (i + 1)
    i += 1
result += ((int(n) - (10 ** length)) + 1) * (length + 1)
print(result)
