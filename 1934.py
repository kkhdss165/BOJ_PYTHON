# 최소공배수 1934
# https://www.acmicpc.net/problem/1934
# 최소공배수(LCM)를 구하시오
# A = a * GCD / B = b * GCD (a,b: 서로소, GCD:최대공약수)
# 최소공배수는 a*b*GCD = A*B/GCD

T = int(input())

for testCase in range(T):
  ab = list(map(int, input().split()))
  A = max(ab)
  B = min(ab)

  X = A
  GCD = B
  
  while X % GCD != 0:
    temp = X % GCD
    X = GCD
    GCD = temp

  print(A*B//GCD)
