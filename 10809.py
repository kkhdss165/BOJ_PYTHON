list = [-1] * 26
a = input()
sum = 0
for index, ch in enumerate(a):
  if list[ord(ch)-97] == -1:
    list[ord(ch)-97] = index

for i in list:
  print(i, end=" ")
