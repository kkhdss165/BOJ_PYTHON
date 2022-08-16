# 약수 1037
# https://www.acmicpc.net/problem/1037
# N개의 약수가 주어질때, A를 구하기
# A는 N개의 약수중 하나 n이 있다고 가정
# A 는 1이 아니고 n이 아님
# max()*min() 부터 max()씩 더해가면서 탐색

_ = int(input())
list = list(map(int, input().split()))

result = max(list) * min(list)

while True:
  for n in list:
    if result % n != 0:
      result += max(list)
      break
  break
  
print(result)
