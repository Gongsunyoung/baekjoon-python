import sys
input = sys.stdin.readline

n = int(input())
cookie = [list(input().strip()) for _ in range(n)]
heart_x, heart_y = 0, 0

for x in range(n):
    for y in range(n):
        if cookie[x][y] == '*':
            if (x > 0 and x < n - 1 and y > 0 and y < n - 1 and
                cookie[x - 1][y] == '*' and cookie[x + 1][y] == '*' and
                cookie[x][y - 1] == '*' and cookie[x][y + 1] == '*'):
                heart_x, heart_y = x, y
                break

print(heart_x + 1, heart_y + 1)

left_arm = 0
for i in range(heart_y - 1, -1, -1):
    if cookie[heart_x][i] == '*':
        left_arm += 1
    else:
        break

right_arm = 0
for i in range(heart_y + 1, n):
    if cookie[heart_x][i] == '*':
        right_arm += 1
    else:
        break

waist = 0
for i in range(heart_x + 1, n):
    if cookie[i][heart_y] == '*':
        waist += 1
    else:
        break

left_leg = 0
for i in range(heart_x + waist + 1, n):
    if cookie[i][heart_y - 1] == '*':
        left_leg += 1
    else:
        break

right_leg = 0
for i in range(heart_x + waist + 1, n):
    if cookie[i][heart_y + 1] == '*':
        right_leg += 1
    else:
        break

print(left_arm, right_arm, waist, left_leg, right_leg)
