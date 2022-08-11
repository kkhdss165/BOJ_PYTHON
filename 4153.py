# 직각삼각형 4153
# https://www.acmicpc.net/problem/4153
# 0 0 0 을 입력받을때 까지 반복
# 세개의 입력 변의 길이를 입력받아 직각삼각형의 유무 출력
while True:
  values = list(map(int, input().split()))
  if values[0] == 0 and values[1] == 0 and values[2] == 0:
    break
  else:
    values.sort()
    if values[0]**2 + values[1]**2 == values[2]**2:
      print("right")
    else:
      print("wrong")
