import sys
n = 1000000
prime = [False, False] + [True] * (n - 1)
for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        for j in range(2 * i, n, i):
            prime[j] = False
for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    count = 0
    for j in range((num//2) + 1):
        if prime[j] and prime[num - j]:
            count += 1
    print(count)
