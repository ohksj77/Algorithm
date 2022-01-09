import sys
e, s, m = map(int, sys.stdin.readline().split())
result = 1
E, S, M = 1, 1, 1
while not (E == e and S == s and M == m):
    if E < 15:
        E += 1
    else:
        E = 1
    if S < 28:
        S += 1
    else:
        S = 1
    if M < 19:
        M += 1
    else:
        M = 1
    result += 1
print(result)
