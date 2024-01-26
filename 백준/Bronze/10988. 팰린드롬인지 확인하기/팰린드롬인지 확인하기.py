s = input()
n = int(len(s) / 2)
c = 1
for i in range(n):
  if s[i] != s[len(s) - i - 1]:
    c = 0
print(c)