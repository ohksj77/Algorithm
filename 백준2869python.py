A, B, V = map(int, input().split())
day = (V - B) / (A - B)
if day % 1 != 0:
    day += 1
print(int(day))
