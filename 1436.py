#666 숫자
#'6'숫자가 3개이상 반복되는 N번째 수 구하기

N = int(input())

n = 665
count = 0
while count < N:
  n = n + 1
  str_n = str(n)
  
  cnt = 0
  for ch in str_n:
    if ch == '6':
      cnt = cnt + 1
      if cnt == 3:
        count = count + 1
        break
    else:
      cnt = 0

print(n)
