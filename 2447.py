#별찍기 - 10
#N은 3의 거듭 제곱
# ***
# * *
# ***
# 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
# 2차원 배열로 생성뒤에, 세션 나누고 출력
# 전체에서 가운데만 제거 (작은 -> 큰)
# size = 1 3으로 나눈 나머지 1일때만
# size = 2 9로 나눈 나머지 345일때만
# size = 3 27로 나눈 나머지 9~17일때만
# python3 시간초과... (PyPy3 성공)

N = int(input())

stars = [[True for j in range(N)] for i in range(N)]

size = 1
while 3**size <= N:
  for i in range(N):
    for j in range(N):
      if (i%(3**size) in range(3**(size-1),2*3**(size-1)) 
          and j % (3**size) in range(3**(size-1),2*3**(size-1))):
        stars[i][j] = False
  size = size + 1

for i in range(N):
  for j in range(N):
    if stars[i][j]:
      print("*",end="")
    else:
      print(" ",end="")
  print()
