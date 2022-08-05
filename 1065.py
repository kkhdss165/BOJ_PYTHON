#한수 = 각자리가 등차수열
#1~2자리 숫자 한수
#범위 1000 이하

n = int(input())
count = 0
for i in range(1, n + 1):
  if i < 100:
    count = count + 1
  else:
    str_i = str(i)
    diff = int(str_i[0]) - int(str_i[1])
    is_han = True
    for a in range(2,len(str_i)):
      if int(str_i[a-1]) - int(str_i[a]) != diff:
        is_han = False
        break
    if is_han:
      count = count + 1
      
print(count)
