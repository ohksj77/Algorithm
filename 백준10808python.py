import sys
string = list(sys.stdin.readline().strip())
arr = [0] * 26
for i in range(len(string)):
    for j in range(ord('a'), ord('z') + 1):
        if ord(string[i]) == j:
            arr[j - ord('a')] += 1
print(*arr)
