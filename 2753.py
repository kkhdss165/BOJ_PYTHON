a = input()

##윤년은 4의 배수, 400의 배수지만, 100의 배수는 아님
if(int(a)%4 == 0 and int(a)%100 != 0) or int(a)%400 == 0 :
  print("1")
else:
  print("0")
