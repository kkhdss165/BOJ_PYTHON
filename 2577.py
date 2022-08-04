total = 1
for i in range(3):
  x = int(input())
  total = total * x
list = list(str(total))

for i in range(10):
  print(list.count(str(i)))
