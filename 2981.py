# 검문 2981
# N개의 숫자가 주어질때 N개의 수의 나머지가 같은 M을 모두 구하시오.
# 6, 34, 38 => 2 4
# 5, 17, 23, 14, 83 => 3
# M은 1보다 크고 M은 제일 작은수 보다 작다 
# A, B, C 가 있다고 가정
# A = a  * M + R
# B = b  * M + R
# C = c  * M + R
# A-B, 하거나 B-C를 하면 R이 사라진다
# A-B와 B-C의 공배수 구하기

def getGCD(a, b):
  num = b
  div = a
  rest = num % div
  while rest!= 0:
    num = div
    div = rest
    rest = num % div

  return div

import sys

N = int(sys.stdin.readline())

values = []
for _ in range(N):
  values.append(int(sys.stdin.readline()))

values.sort()
re_values = [ values[i] - values[i-1] for i in range(1,len(values))]
re_values.sort()

GCD = re_values[0]
for i in range(1, len(re_values)):
  GCD = getGCD(GCD, re_values[i])

result = []
for i in range(2, int(GCD**0.5)+1):
  if GCD % i == 0:
    result.append(i)
    result.append(GCD//i)

result.append(GCD)
print(*sorted(list(set(result))))
