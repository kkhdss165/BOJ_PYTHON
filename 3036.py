# 링 3036
# https://www.acmicpc.net/problem/3036
# 처음 링이 한 바퀴 돌때 다른 링들은 몇바퀴를 도는지 출력
# 8 4 2 = > 2/1, 4/1

def getGCD(a, b):
  x = max(a, b)
  y = min(a, b)
  r = x % y
  while r != 0:
    x = y
    y = r
    r = x % y
  return y

N = int(input())
values = list(map(int, input().split()))

for i in range(1, len(values)):
  a = values[0]
  b = values[i]
  GCD = getGCD(a,b)
  print(str(a//GCD)+"/"+str(b//GCD))
