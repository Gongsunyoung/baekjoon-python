N, K = map(int, input().split())
list = list(input())
count = 0

for i in range(N):
  if list[i] == 'P':
    for j in range(i-K, i+K+1):
      if 0 <= j < N and list[j] == 'H':
        count += 1
        list[j] = 'E'
        break

print(count)