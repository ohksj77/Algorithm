import sys
t = int(sys.stdin.readline())
for _ in range(t):
    sentence = list(sys.stdin.readline().strip().split())
    for word in sentence:
        print(word[::-1], end=' ')
