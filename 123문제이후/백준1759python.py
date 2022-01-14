from itertools import combinations
import sys
l, c = map(int, sys.stdin.readline().split())
arr = sorted(list(sys.stdin.readline().split()))
vowel = ['a', 'e', 'i', 'o', 'u']
for i in combinations(arr, l):
    count = 0
    for j in i:
        if j in vowel:
            count += 1
    if 1 <= count <= l - 2:
        print(''.join(i))
