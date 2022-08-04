list = []
for i in range(10):
  x = int(input()) % 42
  if x not in list:
    list.append(x)

print(len(list))
