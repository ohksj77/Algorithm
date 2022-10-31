import sys
n, m, k = map(int, sys.stdin.readline().split())
def ans(n, m, k):
    arr = list(range(k, 0, -1))
    n -= k
    m -= 1
    while m:
        arr.extend(range(k + n // m, k, -1))
        k += n // m
        n -= n // m
        m -= 1
    return list(map(str, arr))
sys.stdout.write('-1' if n < m + k - 1 or n > m * k else ' '.join(ans(n, m, k)))
