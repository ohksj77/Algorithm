import sys
n = int(sys.stdin.readline())
arr = [0 for _ in range(16)]
result = 0
def check(num):
    for i in range(1, num):
        if arr[num] == arr[i] or abs(arr[num] - arr[i]) == num - i:
            return False
    return True
def dfs(count):
    global result
    if count > n:
        result += 1
    else:
        for i in range(1, n + 1):
            arr[count] = i
            if check(count):
                dfs(count + 1)
dfs(1)
print(result)
