n = int(input())
arr = list(map(int, input().split()))
max = max(arr)
for i in range(n):
    arr[i] = arr[i] / max * 100
print(sum(arr) / n)