import sys
n, b = map(int, sys.stdin.readline().split())
word = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''
while n != 0:
    result += str(word[n % b])
    n //= b
print(result[::-1])
