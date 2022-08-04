orgin = int(input())

count = 0
a = orgin
while True:
  a_1 = a // 10
  a_2 = a % 10

  a = a_2 * 10 + (a_1+a_2)%10
  count = count + 1
  if a == orgin:
    break

print(count)
