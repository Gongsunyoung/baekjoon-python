a = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s = input()
n = 0
for i in range(len(s)):
    for j in a:
        if s[i] in j:
            n += a.index(j) + 3
print(n)