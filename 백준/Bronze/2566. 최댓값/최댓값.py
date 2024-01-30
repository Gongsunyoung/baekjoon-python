max_num = -1
x = 0 
y = 0
a = []
for _ in range(9):
    a.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if a[i][j] > max_num:
            max_num = a[i][j]
            x = i + 1
            y = j + 1
print(max_num)
print(x, y)