import sys

def concatenate(r1, r2):
    return [''.join(x) for x in zip(r1, r2, r1)]
def star(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star(n)
    top_bottom = concatenate(x, x)
    middle = concatenate(x, [' ' * n] * n)
    return top_bottom + middle + top_bottom

print("\n".join(star(int(sys.stdin.readline()))))