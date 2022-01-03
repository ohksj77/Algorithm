import sys
s = list(sys.stdin.readline().rstrip('\n'))
for i in range(len(s)):
    if s[i].isalpha() and s[i].isupper():
        if ord(s[i]) + 13 <= 90:
            s[i] = chr(ord(s[i]) + 13)
        else:
            s[i] = chr(ord(s[i]) - 13)
    elif s[i].isalpha() and s[i].islower():
        if ord(s[i]) + 13 <= 122:
            s[i] = chr(ord(s[i]) + 13)
        else:
            s[i] = chr(ord(s[i]) - 13)
print(''.join(s))
