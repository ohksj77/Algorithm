import sys
calculate = sys.stdin.readline().split("-")
ans = []
for i in calculate:
    cnt = 0
    string = i.split("+")
    for j in string:
        cnt += int(j)
    ans.append(cnt)
res = ans[0]
for i in range(1, len(ans)):
    res -= ans[i]
print(res)
