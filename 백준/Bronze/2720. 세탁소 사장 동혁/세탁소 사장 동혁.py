n = int(input())

for _ in range(n):
    m = int(input())
    for i in [25, 10, 5, 1]:
        print(m//i, end = ' ')
        m = m % i