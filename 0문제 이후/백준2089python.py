import sys
n = int(sys.stdin.readline())
result = ''
if not n:
    print('0')
else:
    while n:
        if n % (-2):
            result = '1' + result
            n = n // -2 + 1
        else:
            result = '0' + result
            n //= -2
sys.stdout.write(result)
