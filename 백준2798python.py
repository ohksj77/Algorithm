import sys
n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
if len(card) == 3:
    print(sum(card))
else:
    card.sort()
    index_s = len(card) - 2
    index_f = index_s - 1
    index_t = index_s + 1
    rng = len(card) * (len(card) - 1) * index_s // 6
    result = 0
    for _ in range(rng):
        temp = card[index_f] + card[index_s] + card[index_t]
        if temp <= m:
            if result < temp:
                result = temp
        if index_f == 0 and index_s == 1 and index_t == 2:
            break
        elif index_f == 0 and index_s == 1:
            index_t -= 1
            index_s = index_t - 1
            index_f = index_s - 1
        elif index_f == 0:
            index_s -= 1
            index_f = index_s - 1
        else:
            index_f -= 1
    print(result)
