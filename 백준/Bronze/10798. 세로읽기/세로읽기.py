word = []
length = []
for _ in range(5):
  word.append(list(input()))
  length.append(len(word[-1]))

s = ''
for i in range(max(length)):
  for j in range(5):
    if i < length[j]:
      s += word[j][i]

print(s)