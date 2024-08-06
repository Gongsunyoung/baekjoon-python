import sys
input = sys.stdin.readline

n, game = input().split()
n = int(n)
li = []

for _ in range(n):
  li.append(input())

unique_li = list(set(li))

if game == 'Y':
  print(len(unique_li))
elif game == 'F':
  print(len(unique_li) // 2)
else:
  print(len(unique_li) // 3)