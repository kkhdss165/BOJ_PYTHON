# 하키 1358
# https://www.acmicpc.net/problem/1358
# 알약 모양의 하키장이 주어진다
# 입력 W H X Y P / P:플레이어수
# 하키장 안에 있는 플레이어의 수를 구하시오.(경계 및 내부)
# 반구 2개, 사각형 1개로 나누어서 포함되는지 구한다

W, H, X, Y, P = map(int, input().split())
radius = H//2
result = 0
for _ in range(P):
  a_x, a_y = map(int, input().split())
  #직사각형
  if (X <= a_x <= X+W) and (Y <= a_y <= Y+H):
    result += 1
  #반구
  elif a_x <= X and ((X - a_x)**2 +  (Y + radius - a_y)**2 <= radius**2):
    result += 1
  elif X+W <= a_x and ((X + W - a_x)**2 + (Y + radius - a_y)**2 <= radius**2):
    result += 1
    
print(result)
