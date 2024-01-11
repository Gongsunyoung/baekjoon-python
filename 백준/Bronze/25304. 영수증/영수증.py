money = int(input())
n = int(input())
sum = 0
for i in range(1, n+1):
    m, c = map(int, input().split())
    sum += m * c

if sum == money:
    print("Yes")
else:
    print("No")