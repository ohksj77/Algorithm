t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if (n / h) % 1 == 0:
        result_w = n // h
        result_h = h
    else:
        result_w = n // h + 1
        result_h = n % h
    print(result_h*100 + result_w)
