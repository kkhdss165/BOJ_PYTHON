# 팩토리얼 0의 개수 1676
# https://www.acmicpc.net/problem/1676
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
# 2와 5의 배수의 갯수 중 min값 구하기
# 5개 단위마다 5의 배수 등장 그런데 2의배수는 5가 한번 등장할때 2개 혹은 3개 등장
# N!의 소인수 분해시 5의 갯수

N = int(input())
count = 0
for i in range(5,N+1,5):
  if i % 5 == 0:
    a = i
    while a % 5 == 0:
      a = a // 5
      count += 1

print(count)
