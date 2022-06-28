import sys
people, num = map(int, sys.stdin.readline().split())
arr = [str(i) for i in range(1, people + 1)]
result = []
index = num - 1
for _ in range(people):
    if index >= len(arr):
        index = index % len(arr)
    result.append(arr.pop(index))
    index += num - 1
print('<', end='')
print(', '.join(result), end='')
print('>')
