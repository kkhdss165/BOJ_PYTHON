# 어린 왕자 1004
# https://www.acmicpc.net/problem/1004
# 시작점과 끝점이 주어지고 n개의 (좌표,좌표, 반지름) 행성계가 주어질때
# 행성 충돌을 최소로 하는 횟수
# 시작점이나 끝 점이 해당 원 안에 있나? >> 해당되면 + 1
# 시작점과 끝점이 둘다 원 안에 있으면 더하지 않는다
# 시작점과 끝점이 둘다 원 밖에 있으면 더하지 않는다
# xor 연산 (둘중에 하나만 걸치면)

T = int(input())
for t in range(T):
  start_x, start_y, end_x, end_y = map(int, input().split())
  n = int(input())
  count = 0
  for i in range(n):
    c_x, c_y, r = map(int, input().split())
    if (bool((start_x - c_x)**2 + (start_y - c_y)**2 < r ** 2)
       ^bool((end_x - c_x)**2 + (end_y - c_y)**2 < r ** 2)):
         count += 1
  print(count)
