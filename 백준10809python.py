import sys
string = list(sys.stdin.readline().strip())
arr = [-1] * 26
for j in range(ord('a'), ord('z') + 1):
    for i in range(len(string)):
        if ord(string[i]) == j:
            arr[j - ord('a')] = i
            break
print(*arr)
