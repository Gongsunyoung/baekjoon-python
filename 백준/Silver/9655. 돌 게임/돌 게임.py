n = int(input())
win = -1

def whose_turn():
    global win
    if win != 0:
        win = 0
    else:
        win = 1

while n != 0:
    if n >= 3:
        n -= 3
    else:
        n -= 1
    whose_turn()

if win == 0:
    print('SK')
else:
    print('CY')
