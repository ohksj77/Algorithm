import sys
n = 1000000
prime = [True] * n
for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        for j in range(2 * i, n, i):
            prime[j] = False
while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break
    flag = False
    for i in range(3, n):
        if prime[i] and prime[num - i]:
            print(num, '=', i, '+', num - i)
            flag = True
            break
    if flag is False:
        print("Goldbach's conjecture is wrong.")
