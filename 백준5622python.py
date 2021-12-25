word = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
sum = 0
for i in range(len(a)):
    for j in word:
        if a[i] in j:
            sum += word.index(j)+3
print(sum)
