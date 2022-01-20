import sys
n = int(sys.stdin.readline())
node = {}
for _ in range(n):
    root, left, right = sys.stdin.readline().rstrip().split()
    node[root] = [left, right]
def pre(root):
    if root != '.':
        print(root, end='')
        pre(node[root][0])
        pre(node[root][1])
def inner(root):
    if root != '.':
        inner(node[root][0])
        print(root, end='')
        inner(node[root][1])
def post(root):
    if root != '.':
        post(node[root][0])
        post(node[root][1])
        print(root, end='')
pre('A')
print()
inner('A')
print()
post('A')
