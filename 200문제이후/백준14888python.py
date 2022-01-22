import sys
n = int(sys.stdin.readline())
num_arr = list(map(int, sys.stdin.readline().split()))
op_arr = list(map(int, sys.stdin.readline().split()))
max_size, min_size = -sys.maxsize - 1, sys.maxsize
def search(num, index, add, sub, mul, div):
    global max_size, min_size
    if index == n:
        max_size = max(max_size, num)
        min_size = min(min_size, num)
        return
    if add:
        search(num + num_arr[index], index + 1, add - 1, sub, mul, div)
    if sub:
        search(num - num_arr[index], index + 1, add, sub - 1, mul, div)
    if mul:
        search(num * num_arr[index], index + 1, add, sub, mul - 1, div)
    if div:
        search(-(-num // num_arr[index]) if num < 0 else num // num_arr[index], index + 1, add, sub, mul, div - 1)
search(num_arr[0], 1 , op_arr[0], op_arr[1], op_arr[2], op_arr[3])
print(max_size)
print(min_size)
