import sys; sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))

    money = 0
    maxPrice = 0

    for index in range(n-1, -1, -1):
        if price[index] > maxPrice:
            maxPrice = price[index]
        else:
            money += maxPrice - price[index]
    
    print(money)