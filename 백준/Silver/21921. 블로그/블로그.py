import sys
input = sys.stdin.readline

n, x = map(int, input().split())
li = list(map(int, input().split()))
high = 0
days = 0

if max(li) == 0:
  print("SAD")
  
else:
  li_temp = sum(li[:x])
  high = li_temp
  days = 1

  for index in range(x, n):
    li_temp -= li[index-x]
    li_temp += li[index]
    if high < li_temp:
      high = li_temp
      days = 1
    elif high == li_temp:
      days += 1

  print(high)
  print(days)