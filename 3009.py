# 네 번째 점 3009
# https://www.acmicpc.net/problem/3009
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
# 4개의 좌표들의 x,y값이 두 번씩 반복 하면 됨

list_x = [] 
list_y = []

for i in range(3):
  x, y = map(int, input().split())
  if x not in list_x:
    list_x.append(x)
  else:
    list_x.remove(x)
  if y not in list_y:
    list_y.append(y)
  else:
    list_y.remove(y)

print(list_x[0], list_y[0])
