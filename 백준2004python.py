import sys
n, m = map(int, sys.stdin.readline().split())
def countnum(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count
five = countnum(n, 5) - countnum(m, 5) - countnum(n - m, 5)
two = countnum(n, 2) - countnum(m, 2) - countnum(n - m, 2)
print(min(five, two))
