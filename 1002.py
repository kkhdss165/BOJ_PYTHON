# 터렛 1002
# https://www.acmicpc.net/problem/1002
# 한 줄에 x1, y1, r1, x2, y2, r2 입력 받는다
# 조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고,
# 조규현이 계산한 류재명과의 거리 r1
# 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수

# 한 점에서 일정 거리 떨어진 점들을 원이라고 한다.
# 같은 점의 경우
# 길이가 같은경우 : 무한대 (-1), 길이가 다른 경우(0)
# 서로 다른 두점의 경우
# r1+r2 > (d2-d1: 두 원의 중심사이의 거리) 이면 접점 2개
# r1+r2 = (d2-d1: 두 원의 중심사이의 거리) 이면 접점 1개(외접)
# r1+r2 < (d2-d1: 두 원의 중심사이의 거리) 이면 접점 0개
# r1-r2 = (d2-d1: 두 원의 중심사이의 거리) 내접
# r1-r2 > (d2-d1: 두 원의 중심사이의 거리) 내부에 있다(만나지 앖는다)
# r1-r2 < (d2-d1: 두 원의 중심사이의 거리) 내부에 있다(두점에서 만난다)
import math

N = int(input())
for i in range(N):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  diff_center = math.sqrt((x1-x2)**2 + (y1-y2)**2)
  sum_radius = r1+r2
  diff_radius = abs(r1-r2)  
  
  if diff_center == 0:
    if r1 == r2:
      print(-1)
    else:
      print(0)
  else:
    if sum_radius == diff_center or diff_radius == diff_center:
      print(1)
    elif diff_radius < diff_center < sum_radius:
      print(2)
    else:
      print(0)
