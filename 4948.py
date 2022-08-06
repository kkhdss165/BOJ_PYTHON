#소수 구하기
#N~2N사이이의 소수 출력 (2N만 포함)
#1. 에라토스테네스의 소수 알고리즘 이용
#2. 반복문을 전체 돌리지 않고 i간격으로 반복

while True:
  N = int(input())
  if N == 0:
    break
  else:
    prime = [True] * (2*N+1)
    
    if 2*N+1 >= 1:
      prime[0] = False
      prime[1] = False
    
    for i in range(2, int((2*N)**0.5)+2):
      if prime[i]:
        for j in range(i + i, 2*N + 1, i):
          prime[j] = False

    count = 0
    for i in range(N+1, 2*N+1):
      if prime[i]:
        count = count + 1

    print(count)
