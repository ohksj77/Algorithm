word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
w = input()
for i in word:
    w = w.replace(i, '*')
print(len(w))
