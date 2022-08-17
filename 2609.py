# 최대공약수와 최소공배수 2609
# https://www.acmicpc.net/problem/2609
# 두 수의 최대공약수(GCD), 최소공배수(LCM)를 구하시오
# 약수들을 모두 구해서 카운팅
# Counter를 이용한 방법

from collections import Counter

A, B = map(int, input().split())
list_A = []
list_B = []

n = 2
while A != 1:
  if A % n == 0:
    while A % n == 0:
      A /= n
      list_A.append(n)
  n += 1    

n = 2
while B != 1:
  if B % n == 0:
    while B % n == 0:
      B /= n
      list_B.append(n)
  n += 1    

dict_A = Counter(list_A)
dict_B = Counter(list_B)

GCD = 1
for a, a_n in dict_A.items():
  if a in list_B:
    GCD *= a ** min(a_n,dict_B[a])
print(GCD)

LCM = 1
for a, a_n in dict_A.items():
  if a in list_B:
    LCM *= a ** max(a_n,dict_B[a])
  else:
    LCM *= a ** a_n

for b, b_n in dict_B.items():
  if b not in list_A:
    LCM *= b ** b_n

print(LCM)
