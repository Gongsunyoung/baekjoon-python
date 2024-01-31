area = [[0] * 100 for _ in range(100)]
n = int(input())
size = n * 100
cnt = 0
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if area[i][j] == 0:
                area[i][j] = 1
            else:
              cnt += 1
print(size - cnt)