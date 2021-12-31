import sys
t = int(sys.stdin.readline())
arr = []
for i in range(t):
    age, name = sys.stdin.readline().split()
    name = name.strip()
    age = int(age)
    arr.append((age, name, i))
arr.sort(key=lambda x: (x[0], x[2]))
for age, name, num in arr:
    print(age, name)
