#소수 구하기
#N~M사이이의 소수 출력 (N,M 포함)
#기존방법으로 하면 시간 초과
#1. 에라토스테네스의 소수 알고리즘 이용
#2. 반복문을 전체 돌리지 않고 i간격으로 반복


import sys

N, M = map(int, sys.stdin.readline().split())
prime = [True] * (M+1)


if M >= 1:
  prime[0] = False
  prime[1] = False

for i in range(2, int(M**0.5)+2):
  if prime[i]:
    for j in range(i + i, M+1, i):
      prime[j] = False

for i in range(N, M+1):
  if prime[i]:
    print(i)
