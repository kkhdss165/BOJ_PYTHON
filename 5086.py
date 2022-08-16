# 배수와 약수 5086
# https://www.acmicpc.net/problem/5086

while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break
  else:
    if a < b and b % a == 0:
      print("factor")
    elif b < a and a % b == 0:
      print("multiple")
    else:
      print("neither")
