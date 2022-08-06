#골드바흐 추측
#골드바흐 : 2보다 큰 짝수는 소수 + 소수로 나타내는것이 가능
#2보다 큰 짝수 n이 주어졌을 때(n>=4)
##만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
# n = 8, 3 + 5
# n = 10, 5 + 5
# n = 16, 5 + 11

#n보다 작은 소수 구하기
#소수 배열 만들기
#소수 배열에서 조합 구하기

import sys

testCase = int(sys.stdin.readline())

for t in range(testCase):
  n = int(sys.stdin.readline())

  #n보다 작은 소수 구하기
  prime = [True] * (n+1)
  prime[0] = False
  prime[1] = False
  for i in range(2,int(n**0.5)+2):

    for j in range(i+i, n+1 ,i):
      prime[j] = False

  #소수 배열 만들기
  prime_list = []
  for i in range(n+1):
    if prime[i]:
      prime_list.append(i)
      
  #소수 배열에서 조합 구하기
  prime_combi = []
  for i in prime_list:
    if n-i in prime_list and (i, n-i):
      prime_combi.append((i, n-i))

  #인덱스: 2개인경우 0, 3개인 경우 1, 4개인 경우 1
  print(prime_combi[(len(prime_combi)-1)//2][0], prime_combi[(len(prime_combi)-1)//2][1])
