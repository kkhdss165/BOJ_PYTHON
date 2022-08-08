#김정인 버전 블랙잭
#N장의 주어진 카드들로 M을 넘지않는 가장 큰 카드 3장의 합 구하기
# 3 =< N <= 100
# 카드 3개를 선택하는 방법
# 5c3 = 5*4*3/(3*2*1) = 10

from itertools import combinations

N, M = map(int, input().split())
values = list(map(int, input().split()))

sums =[]

for i in combinations(values, 3):
  if sum(i) <= M:
    sums.append(sum(i))

print(max(sums))
