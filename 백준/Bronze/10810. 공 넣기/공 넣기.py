n, m = map(int, input().split())
arr = [0] * (n+1)

for _ in range(m):
    i, j, k = map(int, input().split())
    for y in range(i, j+1):
        arr[y] = k
for z in range(1, n+1):
    print(arr[z], end=" ")
