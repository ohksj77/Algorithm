import sys
word = sys.stdin.readline().strip()
arr = []
for i in range(len(word)):
    arr.append(word[i:])
arr.sort()
print("\n".join(arr))
