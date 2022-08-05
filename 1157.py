count = [0] * 26

a = input()
for i in a:
  count[ord(i.upper())-65] = count[ord(i.upper())-65] + 1
  
max_value = max(count)
max_indexs = list(filter(lambda x: count[x] == max_value, range(len(count))))

if len(max_indexs) == 1:
  print(chr(max_indexs[0] + 65))
else:
  print("?")
