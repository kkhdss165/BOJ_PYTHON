# 패션왕 신해빈 9375
# https://www.acmicpc.net/problem/9375
# (의류 종류의수 + 1)씩 곱하고 하나도 안꼈을때 1을 빼면 됨
# ex 안경 2개 모자 2개면 (2 + 1) * (2 + 1) - 1

from collections import Counter
T = int(input())

for _ in range(T):
  N = int(input())
  products = []
  for _ in range(N):
    p_name, p_type = input().split()
    products.append(p_type)
  count = Counter(products)
  result = 1
  for p_name, p_num in count.most_common():
    result *= (p_num + 1)
  result -= 1
  print(result)
