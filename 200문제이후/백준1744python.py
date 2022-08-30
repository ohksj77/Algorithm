import sys
n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
pos, neg, res = [], [], 0
for i in nums:
    if i > 0:
        pos.append(i)
    else:
        neg.append(i)
pos.sort()
neg.sort(reverse=True)
while len(pos) > 1:
    fir, sec = pos.pop(), pos.pop()
    if fir == 1 or sec == 1:
        res += fir + sec
    else:
        res += fir * sec
if pos:
    res += pos.pop()
while len(neg) > 1:
    fir, sec = neg.pop(), neg.pop()
    res += fir * sec
if neg:
    res += neg.pop()
sys.stdout.write(str(res))

