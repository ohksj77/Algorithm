num = int(input())
count = 0
for _ in range(num):
    word = input()
    flag = True
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            newWord = word[i + 1:]
            if newWord.count(word[i]) > 0:
                flag = False
    if flag == True:
        count += 1
print(count)
