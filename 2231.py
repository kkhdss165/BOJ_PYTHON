#분해합
#256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 
#자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
#정수 N 에대해서 생성자 abc가 있다고 가정
#a+b+c <= 27이므로
#3자리 인 경우 N-27부터 탐색?
#1자리 인 경우 N-9부터 탐색? (0부터 탐색)


N = int(input())

#n의 자리수
n_nums = 1
while 10**n_nums <= N:
  n_nums = n_nums + 1

result = None
for i in range(max(N - 9*n_nums,0), N):
  sum = i
  temp = i
  for j in range(n_nums):
    sum = sum + temp%10
    temp = temp // 10
  if sum == N:
    result = i
    break

if result != None:
  print(result)
else:
  print(0)
